import psycopg2


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='postgres')
    return conn
