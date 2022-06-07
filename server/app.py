from urllib import response
import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


TODO = [
    {
        'task': 'Feed cats',
        'author': 'Adrian',
        'done': True,
        'id': uuid.uuid4().hex
    },
    {
        'task': 'Make food',
        'author': 'Adrian',
        'done': False,
        'id': uuid.uuid4().hex
    },
    {
        'task': 'Fix brain',
        'author': 'Janick',
        'done': False,
        'id': uuid.uuid4().hex
    }
]


@app.route('/todo', methods=['GET', 'POST'])
def all_todo():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        TODO.append({
            'task': post_data.get('task'),
            'author': post_data.get('author'),
            'done': post_data.get('done'),
            'id': uuid.uuid4().hex
        })
        response_object['message'] = 'Task added!'
    else:
        response_object['todo'] = TODO
    return jsonify(response_object)


# Add case if the id is not existing or Payload not correct.
@app.route('/todo/<todo_id>', methods=['PUT', 'DELETE'])
def single_todo(todo_id):
    response_object = {'staus': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_todo(todo_id)
        TODO.append({
            'task': post_data.get('task'),
            'author': post_data.get('author'),
            'done': post_data.get('done'),
            'id': uuid.uuid4().hex
        })
        response_object['message'] = 'Task updated!'
    if request.method == 'DELETE':
        remove_todo(todo_id)
        response_object['message'] = 'Task removed!'
    return jsonify(response_object)


def remove_todo(todo_id):
    for todo in TODO:
        if todo['id'] == todo_id:
            TODO.remove(todo)
            return True
    return False


if __name__ == '__main__':
    app.run()
