class DBPropertyUtil:
    @staticmethod
    def get_connection_string():
        server_name = "SAMAR\\MSSQLSERVER01"
        database_name = "LMSDB"
        driver = "SQL Server"

        return f"DRIVER={{{driver}}};SERVER={server_name};DATABASE={database_name};Trusted_Connection=yes"
