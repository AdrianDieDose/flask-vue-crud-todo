from urllib import response
import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
from config import config
from psycopg2.extras import RealDictCursor
import json


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


TODO = []
# TODO = [
#     {
#         'task': 'Feed cats',
#         'author': 'Adrian',
#         'done': True,
#         'id': uuid.uuid4().hex
#     },
#     {
#         'task': 'Make food',
#         'author': 'Adrian',
#         'done': False,
#         'id': uuid.uuid4().hex
#     },
#     {
#         'task': 'Fix brain',
#         'author': 'Janick',
#         'done': False,
#         'id': uuid.uuid4().hex
#     }
# ]


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

        getData()
        print(TODO)
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


# Database connection:
def getData():
    # Connect to the PostgresSQL database server
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL databse...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor(cursor_factory=RealDictCursor)

        # Print table content
        # print('PostgresSQL city:')
        cur.execute('SELECT task, author, done FROM todos')
        # Clears array because of reload dupplication
        TODO.clear()
        for result in cur.fetchall():
            #res = dict([(key, value) for key, value in r])

            TODO.append(result)
            print('GOT DATA')
           # print(json.dumps(result))

        # Print db version
        '''
        print('PostgresSQL database version:')
        cur.execute('SELECT version()')
        
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
        '''

        # close the communication with PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Databse conenction closed.')


def setData():
    # Connect to the PostgresSQL database server
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL databse...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor(cursor_factory=RealDictCursor)

        # SQL FOR: PUT / UPDATE

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Databse conenction closed.')


if __name__ == '__main__':
    app.run()
