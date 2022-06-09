import os
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="flask_db",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS todos;')
cur.execute('CREATE TABLE todos (id uuid PRIMARY KEY,'
            'task text NOT NULL,'
            'author text NOT NULL,'
            'done boolean,'
            'date_added date DEFAULT CURRENT_TIMESTAMP);'
            )

# Insert data into the table
id = 'c69fd51e40f145ddbd6c07958cd70451'
task = 'Go sleep'
author = 'me'
done = 'true'

cur.execute('INSERT INTO todos (id, task, author, done)'
            'VALUES (%s, %s, %s, %s)',
            (id,
             task,
             author,
             done)
            )


conn.commit()

cur.close()
conn.close()
