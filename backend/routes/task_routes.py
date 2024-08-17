from flask import Blueprint, request, jsonify
from models.task import Task, db

# Crear un blueprint para las rutas de tareas
task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Obtener todas las tareas.
    Retorna una lista de todas las tareas en formato JSON.
    """
    try:
        tasks = Task.query.all()
        return jsonify([{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    """
    Crear una nueva tarea.
    Recibe un JSON con 'title' y 'description', y crea una nueva tarea en la base de datos.
    Retorna el ID de la nueva tarea creada.
    """
    try:
        data = request.json
        new_task = Task(title=data['title'], description=data['description'])
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'id': new_task.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@task_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    """
    Actualizar una tarea existente.
    Recibe un ID de tarea y un JSON con 'title' y 'description'.
    Actualiza la tarea en la base de datos y retorna un mensaje de éxito.
    """
    try:
        task = Task.query.get_or_404(id)
        data = request.json
        task.title = data['title']
        task.description = data['description']
        db.session.commit()
        return jsonify({'message': 'Task updated'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@task_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    """
    Eliminar una tarea existente.
    Recibe un ID de tarea, elimina la tarea de la base de datos y retorna un mensaje de éxito.
    """
    try:
        task = Task.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
