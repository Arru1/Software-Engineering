import sqlite3

class DatabaseConnection:
    _instance = None
    _connection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            # Initialize the connection here
            cls._connection = sqlite3.connect('app.db')
            cls._connection.row_factory = sqlite3.Row  # Optionally set row factory to return rows as dictionaries
        return cls._instance

    def get_connection(self):
        return self._connection

    def close(self):
        if self._connection:
            self._connection.close()
            self._connection = None
