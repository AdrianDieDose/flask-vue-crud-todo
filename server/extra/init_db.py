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
cur.execute('CREATE TABLE todos (id serial PRIMARY KEY,'
            'task varchar (150) NOT NULL,'
            'author varchar (50) NOT NULL,'
            'done boolean,'
            'date_added date DEFAULT CURRENT_TIMESTAMP);'
            )

# Insert data into the table

cur.execute('INSERT INTO todos (task, author, done)'
            'VALUES (%s, %s, %s)',
            ('Work at Sit&Watch',
             'Adrian!',
             'false')
            )


cur.execute('INSERT INTO todos (task, author, done)'
            'VALUES (%s, %s, %s)',
            ('Get Candy',
             'Janick!',
             'false')
            )

conn.commit()

cur.close()
conn.close()
