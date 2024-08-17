<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8" lg="6">
        <v-form @submit.prevent="addTask">
          <v-text-field
            v-model="newTask.title"
            label="Title"
            required
            outlined
          ></v-text-field>
          <v-textarea
            v-model="newTask.description"
            label="Description"
            required
            outlined
          ></v-textarea>
          <v-btn color="primary" type="submit" block>Add Task</v-btn>
        </v-form>
      </v-col>
    </v-row>

    <v-row justify="center" class="q-gutter-sm">
      <v-col
        v-for="task in tasks"
        :key="task.id"
        cols="12"
        md="6"
        lg="4"
        v-intersect="{
          handler: (entries) => onIntersect(entries, task),
          options: { threshold: 0.1 },
        }"
      >
        <transition name="scale">
          <v-card
            v-if="task.isVisible"
            class="example-item"
            flat
            bordered
            elevation="2"
          >
            <v-card-title>{{ task.title }}</v-card-title>
            <v-card-subtitle>{{ task.description }}</v-card-subtitle>
            <v-card-actions>
              <v-btn text @click="editTask(task)"> Edit </v-btn>
              <v-btn text @click="deleteTask(task.id)"> Delete </v-btn>
            </v-card-actions>
          </v-card>
        </transition>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useTaskStore } from "../stores/taskStore";

const taskStore = useTaskStore();

const newTask = ref({ title: "", description: "" });
const tasks = computed(() =>
  taskStore.tasks.map((task) => ({ ...task, isVisible: false }))
);

const fetchTasks = () => {
  taskStore.fetchTasks().then(() => {
    tasks.value.forEach((task, index) => {
      setTimeout(() => {
        task.isVisible = true;
      }, index * 100);
    });
  });
};

const onIntersect = (entries, task) => {
  if (Array.isArray(entries)) {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        task.isVisible = true;
      }
    });
  } else {
    if (entries.isIntersecting) {
      task.isVisible = true;
    }
  }
};

const addTask = () => {
  if (taskStore.editingTask) {
    taskStore.updateTask(taskStore.editingTask.id, newTask.value);
  } else {
    taskStore.addTask(newTask.value);
  }
  newTask.value = { title: "", description: "" };
  taskStore.editingTask = null;
};

const editTask = (task) => {
  newTask.value = { title: task.title, description: task.description };
  taskStore.editingTask = task;
};

const deleteTask = (id) => {
  taskStore.deleteTask(id);
};

onMounted(fetchTasks);
</script>

<style scoped>
.example-item {
  height: 150px;
  width: 290px;
  margin: 10px auto;
}

.scale-enter-active,
.scale-leave-active {
  transition: transform 0.5s ease;
}

.scale-enter,
.scale-leave-to {
  transform: scale(0.8);
}
</style>
