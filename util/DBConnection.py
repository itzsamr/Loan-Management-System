import pyodbc
from DBPropertyUtil import DBPropertyUtil


class DBConnUtil:
    @staticmethod
    def get_connection():
        connection_string = DBPropertyUtil.get_connection_string()
        try:
            connection = pyodbc.connect(connection_string)
            print("Connected to database successfully")
            return connection
        except pyodbc.Error as e:
            print(f"Error while connecting to SQL database: {e}")
            return None
