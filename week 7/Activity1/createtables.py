import sqlite3

def create_tables():
    conn = sqlite3.connect('app.db')  # Connect to the SQLite database
    cursor = conn.cursor()

    # Create users table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    ''')

    # Create orders table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        product TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')

    conn.commit()  # Commit changes to the database
    conn.close()   # Close the connection

# Call the function to create the tables
create_tables()
