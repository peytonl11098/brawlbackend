from flask import Blueprint, request, jsonify
from model.taskmanager import ToDoTask  # Importing ToDoTask class from the taskmanager module
# Creating a Blueprint named 'todo_api' with a URL prefix '/api/todo'
todo_api = Blueprint('todo_api', __name__, url_prefix='/api/todo')
tasks = []  # List to store tasks
# Route to add a new task via POST method
@todo_api.route('/add', methods=['POST'])
def add_task():
    data = request.get_json()  # Extracting JSON data from the request
    description = data.get('description')  # Retrieving task description from the JSON data
    date = data.get('date')  # Retrieving task date from the JSON data
    time = data.get('time')  # Retrieving task time from the JSON data
    task = ToDoTask(description, date, time)  # Creating a new ToDoTask object with the provided details
    tasks.append(task)  # Adding the task to the tasks list
    return jsonify({'message': 'Task added successfully'})  # Returning a JSON response indicating success
# Route to list all tasks via GET method
@todo_api.route('/list', methods=['GET'])
def list_tasks():
    # Creating a list of dictionaries containing task details (description, completion status, date, time) for each task
    task_list = [{'description': task.description, 'completed': task.completed, 'date': task.date, 'time': task.time} for task in tasks]
    return jsonify(task_list)  # Returning the list of tasks as a JSON response
# Route to mark a task as completed via PUT method
@todo_api.route('/complete/<string:description>', methods=['PUT'])
def complete_task(description):
    # Finding the index of the task with the provided description
    task_index = next((i for i, task in enumerate(tasks) if task.description == description), None)
    if task_index is not None:  # If the task is found
        tasks[task_index].completed = True  # Marking the task as completed
        return jsonify({'message': 'Task completed successfully'})  # Returning a JSON response indicating success
    else:
        return jsonify({'message': 'Task not found'}), 404  # Returning a JSON response indicating that the task was not found
# Route to delete a task via DELETE method
@todo_api.route('/delete/<string:description>', methods=['DELETE'])
def delete_task(description):
    # Finding the index of the task with the provided description
    task_index = next((i for i, task in enumerate(tasks) if task.description == description), None)
    if task_index is not None:  # If the task is found
        del tasks[task_index]  # Deleting the task from the tasks list
        return jsonify({'message': 'Task deleted successfully'})  # Returning a JSON response indicating success
    else:
        return jsonify({'message': 'Task not found'}), 404  # Returning a JSON response indicating that the task was not found