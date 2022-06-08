import psycopg2
from config import config
from psycopg2.extras import RealDictCursor
import json

# TO START THE DB: "SUDO SERVICE POSTGRESQL START"


def connect():
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
        TODO = cur.fetchall()
        print(TODO)

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


if __name__ == '__main__':
    connect()
