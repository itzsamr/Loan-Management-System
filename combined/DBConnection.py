import pyodbc
import configparser


class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            connection_string = DBConnection.get_connection_string()
            try:
                DBConnection.connection = pyodbc.connect(connection_string)
                print("Connected to database successfully")
            except pyodbc.Error as e:
                print(f"Error while connecting to SQL database: {e}")
        return DBConnection.connection

    @staticmethod
    def get_connection_string():
        config = configparser.ConfigParser()
        config.read(
            "C:/Users/91915/OneDrive - Valliammai Engineering College/Desktop/CarRentalSystem/LoanManagementSystem/combined/config.properties"
        )
        server_name = config.get("DATABASE", "server")
        database_name = config.get("DATABASE", "database")
        driver = config.get("DATABASE", "driver")
        return f"DRIVER={{{driver}}};SERVER={server_name};DATABASE={database_name};Trusted_Connection=yes"
