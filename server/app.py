from urllib import response
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
        'done': True
    },
    {
        'task': 'Make food',
        'author': 'Adrian',
        'done': False
    },
    {
        'task': 'Fix brain',
        'author': 'Janick',
        'done': False
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
            'done': post_data.get('done')
        })
        response_object['message'] = 'Task added!'
    else:
        response_object['todo'] = TODO
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
