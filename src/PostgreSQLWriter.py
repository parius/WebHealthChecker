import psycopg2

class PostgreSQLWriter:
    def __init__(self, settings):
        self.connection = psycopg2.connect(user = settings.getDBUser(),
                                    password = settings.getDBPassword(),
                                    host = settings.getDBHost(),
                                    port = settings.getDBPort(),
                                    database = settings.getDBDatabase())
        self.create_table()

    def create_table(self):
        cursor = self.connection.cursor()
    
        create_table_query = '''CREATE TABLE IF NOT EXISTS health_status (
            id            SERIAL,
            timestamp     TIMESTAMP NOT NULL,
            url           TEXT NOT NULL,
            code          TEXT NOT NULL,
            response_time INTEGER NOT NULL
            ); '''
        
        cursor.execute(create_table_query)
        self.connection.commit()

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()
    
    def send(self, data):
        print("PostgreSQLWriter writing data to DB:", data)
        record = data
        query = """ INSERT INTO health_status (timestamp, url, code, response_time) VALUES (%s,%s,%s,%s)"""
        cursor = self.connection.cursor()
        cursor.execute(query, record)
        self.connection.commit()