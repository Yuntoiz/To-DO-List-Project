import socket

from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from flask import Flask, render_template

from utils import load_json, save_json, search

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

tasks_data = load_json('tasks')

# Get all tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
  sort_by = request.args.get('sort_by', 'id')
  sorted_tasks = sorted(tasks_data, key=lambda k: k[sort_by])
  # if search_key and len(search_key)>0:
  #     sorted_tasks= search(sorted_tasks,search_key)
  response = jsonify(sorted_tasks)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response


# Get a task by ID
@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
  task = next((item for item in tasks_data if item["id"] == task_id), None)
  if task:
    response = jsonify(task)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
  else:
    response = jsonify({"message": "Task not found"}), 404
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# Add a new task
@app.route('/api/tasks', methods=['POST'])
def add_task():
  task = request.json
  task['id'] = len(tasks_data) + 1
  tasks_data.append(task)
  save_json(name='tasks', data=tasks_data)
  response = jsonify(tasks_data)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response


# Delete a task by ID
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
  task = next((item for item in tasks_data if item["id"] == task_id), None)
  if task:
    tasks_data.remove(task)
    save_json(name='tasks', data=tasks_data)
    response = jsonify({"message": "Task deleted successfully"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
  else:
    response = jsonify({"message": "Task not found"}), 404
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


with open('data/personalGoals.json') as f:
  goals = json.load(f)


# Get all goals
@app.route('/api/goals', methods=['GET'])
def get_goals():
  sort_by = request.args.get('sort_by', 'id')
  sorted_goals = sorted(goals, key=lambda k: k[sort_by])
  response = jsonify(sorted_goals)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response


# Get a task by ID
@app.route('/api/goals/<int:goal_id>', methods=['GET'])
def get_goal(goal_id):
  goal = next((item for item in goals if item["id"] == goal_id), None)
  if goal:
    response = jsonify(goal)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
  else:
    response = jsonify({"message": "goal not found"}), 404
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# Add a new goal
@app.route('/api/goals', methods=['POST'])
def add_goal():
  goal = request.json
  goal['id'] = len(goals) + 1
  goals.append(goal)
  response = jsonify(goal)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response


# Delete a goal by ID
@app.route('/api/goals/<int:goal_id>', methods=['DELETE'])
def delete_goal(goal_id):
  goal = next((item for item in goals if item["id"] == goal_id), None)
  if goal:
    goals.remove(goal)
    response = jsonify({"message": "goal deleted successfully"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
  else:
    response = jsonify({"message": "goals not found"}), 404
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# handle pages
@app.route('/', methods=['GET'])
# @app.route('/index', methods=['GET'])
def index():
  return render_template('main.html')  #


@app.route('/personal_goals')
def personal_goals():
  host = "https://todo-app.pretmas.repl.co/api"
  return render_template('personal_goals.html', host=host) #RENDERS HTML TEMPLATES


@app.route('/tasks')
def tasks():
  host = "https://todo-app.pretmas.repl.co/api"
  return render_template('tasks.html', host=host)  #RENDERS HTML TEMPLATES


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
