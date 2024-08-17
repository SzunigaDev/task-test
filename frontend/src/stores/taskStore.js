import { defineStore } from 'pinia';
import axios from 'axios';

export const useTaskStore = defineStore('taskStore', {
  state: () => ({
    tasks: [],
  }),
  actions: {
    async fetchTasks() {
      try {
        const response = await axios.get('http://localhost:5000/tasks');
        this.tasks = response.data;
      } catch (error) {
        console.error('Error fetching tasks:', error);
      }
    },
    async addTask(task) {
      try {
        await axios.post('http://localhost:5000/tasks', task);
        this.fetchTasks();
      } catch (error) {
        console.error('Error adding task:', error);
      }
    },
    async deleteTask(id) {
      try {
        await axios.delete(`http://localhost:5000/tasks/${id}`);
        this.fetchTasks();
      } catch (error) {
        console.error('Error deleting task:', error);
      }
    },
  },
});
