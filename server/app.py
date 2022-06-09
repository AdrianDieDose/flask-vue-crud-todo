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


@app.route('/todo', methods=['GET', 'POST'])
def all_todo():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        insertData(uuid.uuid4().hex, post_data.get('task'), post_data.get('author'),
                   post_data.get('done'))
        response_object['message'] = 'Task added!'
    else:
        getData()
        # print(TODO)
        response_object['todo'] = TODO
    return jsonify(response_object)


# Add case if the id is not existing or Payload not correct.
@app.route('/todo/<todo_id>', methods=['PUT', 'DELETE'])
def single_todo(todo_id):
    response_object = {'staus': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        updateData(todo_id, post_data.get('task'), post_data.get('author'),
                   post_data.get('done'))
        response_object['message'] = 'Task updated!'
    if request.method == 'DELETE':
        removeData(todo_id)
        response_object['message'] = 'Task removed!'
    return jsonify(response_object)


# Database connection:
def getData():
    # Connect to the PostgresSQL database server
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL databse for read...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor(cursor_factory=RealDictCursor)

        # Executes statement
        cur.execute('SELECT id, task, author, done FROM todos')
        # Clears array because of reload dupplication
        TODO.clear()
        for result in cur.fetchall():
            TODO.append(result)
            print('GOT DATA')
           # print(json.dumps(result))

        # close the communication with PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Databse conenction closed.')


# Database write:
def insertData(id, task, author, done):
    # Connect to the PostgresSQL database server
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL databse...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        cur.execute('INSERT INTO todos (id, task, author, done)'
                    'VALUES (%s, %s, %s, %s)',
                    (id,
                     task,
                     author,
                     done)
                    )

        conn.commit()
        # close the communication with PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Databse conenction closed.')


# Database remove:
def removeData(todoID):
    # Connect to the PostgresSQL database server
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL databse for delete...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        cur.execute(f"DELETE FROM todos WHERE id = '{todoID}';")

        conn.commit()
        # close the communication with PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Databse conenction closed.')


def updateData(id, task, author, done):
    # Connect to the PostgresSQL database server
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL databse...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        print(
            f"UPDATE todos SET task = '{task}', author = '{author}', done = '{done}' WHERE id = '{id}';")
        cur.execute(
            f"UPDATE todos SET task = '{task}', author = '{author}', done = '{done}' WHERE id = '{id}';")

        conn.commit()
        # close the communication with PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Databse conenction closed.')


if __name__ == '__main__':
    #insertData('4626246', 'Save me', 'Friends', 'false')
    app.run()
