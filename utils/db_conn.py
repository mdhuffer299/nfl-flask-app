import psycopg2
import logging


class Client:
    def __init__(self, host='localhost', database='postgres'):
        self.host = host
        self.database = database
        self.conn = None
        self.cursor = None
        self.open_conn()

    def open_conn(self):
        try:
            self.conn = psycopg2.connect(host=self.host,
                                         database=self.database)
            self.cursor = self.conn.cursor()
        except psycopg2.OperationalError as err:
            logging.error(err)

        return self

    def close_conn(self):
        self.conn.close()
        self.cursor.close()

        return "Closed Connection"

    def query(self, query):
        db = self.open_conn()
        db.cursor.execute(query)
        query_results = db.cursor.fetchall()

        return query_results

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
