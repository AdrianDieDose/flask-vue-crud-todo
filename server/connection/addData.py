import os
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="flask_db",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()


# Insert data into the table

cur.execute('INSERT INTO todos (task, author, done)'
            'VALUES (%s, %s, %s)',
            ('Get Candy',
             'Janick!',
             'false')
            )


conn.commit()

cur.close()
conn.close()
