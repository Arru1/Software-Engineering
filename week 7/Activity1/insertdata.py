import sqlite3

def insert_sample_data():
    conn = sqlite3.connect('app.db')  # Connect to the SQLite database
    cursor = conn.cursor()

    # Insert some sample users
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Aruna', 'aruna@example.com'))
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Mayalu', 'mayalu@example.com'))
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Kanxu', 'kanxu@example.com'))

    # Insert some sample orders for user_id 1 and 2
    cursor.execute("INSERT INTO orders (user_id, product, quantity) VALUES (?, ?, ?)", (1, 'Laptop', 1))
    cursor.execute("INSERT INTO orders (user_id, product, quantity) VALUES (?, ?, ?)", (1, 'Mouse', 2))
    cursor.execute("INSERT INTO orders (user_id, product, quantity) VALUES (?, ?, ?)", (2, 'Phone', 1))

    conn.commit()  # Commit changes to the database
    conn.close()   # Close the connection

# Call the function to insert data
insert_sample_data()
