import psycopg2
from psycopg2.extras import RealDictCursor
import os



class DatabaseService:

    def get_connection(self):
        return psycopg2.connect(
            host=os.environ["HOST"],
            database=os.environ["DATABASE"],
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            port=os.environ["PORT"],
            cursor_factory=RealDictCursor
    )



databaseService = DatabaseService()

