from activity1db import DatabaseConnection  # Import the Singleton connection

import time

class UserService:
    def get_user(self, user_id):
        start_time = time.time()
        conn = DatabaseConnection().get_connection()  # Use the Singleton connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()  # Get the first matching user
        end_time = time.time()
        print(f"get_user took {end_time - start_time} seconds")
        return result

class OrderService:
    def get_orders(self, user_id):
        start_time = time.time()
        conn = DatabaseConnection().get_connection()  # Use the Singleton connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        result = cursor.fetchall()  # Get all orders for the user
        end_time = time.time()
        print(f"get_orders took {end_time - start_time} seconds")
        return result

# Test the UserService and OrderService
if __name__ == "__main__":
    user_service = UserService()
    order_service = OrderService()

    # Fetch user with ID 1
    user = user_service.get_user(1)
    if user:
        print(f"User Info: {dict(user)}")  # Convert to dictionary for better readability
    else:
        print("User not found.")

    # Fetch orders for user with ID 1
    orders = order_service.get_orders(1)
    if orders:
        print("Orders for User 1:")
        for order in orders:
            print(dict(order))  # Convert to dictionary for better readability
    else:
        print("No orders found.")
