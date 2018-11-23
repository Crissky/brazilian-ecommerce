import pymysql


class DatabaseHelper:

    class __DatabaseConnection:
        def __init__(self, db_host, db_port, db_name, db_user, db_password):
            self.DB_HOST = db_host
            self.DB_PORT = db_port
            self.DB_NAME = db_name
            self.DB_USER = db_user
            self.DB_PASSWORD = db_password

        def connect(self):
            conn = pymysql.connect(
                host=self.DB_HOST,
                port=self.DB_PORT,
                user=self.DB_USER,
                password=self.DB_PASSWORD,
                db=self.DB_NAME,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            return conn

    __DB_HOST = 'localhost'
    __DB_PORT = 3306
    __DB_NAME = 'data-science'
    __DB_USER = 'root'
    __DB_PASSWORD = ''
    __instance = None

    @staticmethod
    def get_instance():
        if not DatabaseHelper.__instance:
            DatabaseHelper.__instance = DatabaseHelper.__DatabaseConnection(
                DatabaseHelper.__DB_HOST,
                DatabaseHelper.__DB_PORT,
                DatabaseHelper.__DB_NAME,
                DatabaseHelper.__DB_USER,
                DatabaseHelper.__DB_PASSWORD
            ).connect()

        return DatabaseHelper.__instance
