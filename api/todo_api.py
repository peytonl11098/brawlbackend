from flask import Blueprint, request, jsonify
from model.taskmanager import ToDoTask  
todo_api = Blueprint('todo_api', __name__, url_prefix='/api/todo')
tasks = []  

@todo_api.route('/add', methods=['POST'])
def add_task():
    data = request.get_json()  
    description = data.get('description')  
    date = data.get('date')  
    time = data.get('time')  
    task = ToDoTask(description, date, time)  
    tasks.append(task)  
    return jsonify({'message': 'Task added successfully'})  

@todo_api.route('/list', methods=['GET'])
def list_tasks():
    task_list = [{'description': task.description, 'completed': task.completed, 'date': task.date, 'time': task.time} for task in tasks]
    return jsonify(task_list)  

@todo_api.route('/complete/<string:description>', methods=['PUT'])
def complete_task(description):
    task_index = next((i for i, task in enumerate(tasks) if task.description == description), None)
    if task_index is not None:  
        tasks[task_index].completed = True  
        return jsonify({'message': 'Task completed successfully'})  
    else:
        return jsonify({'message': 'Task not found'}), 404  

@todo_api.route('/delete/<string:description>', methods=['DELETE'])
def delete_task(description):
    task_index = next((i for i, task in enumerate(tasks) if task.description == description), None)
    if task_index is not None:  
        del tasks[task_index]  
        return jsonify({'message': 'Task deleted successfully'})  
    else:
        return jsonify({'message': 'Task not found'}), 404  
