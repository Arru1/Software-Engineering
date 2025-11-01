#Develop a Python project that uses the "time.sleep" method together with a decorator to measure a function’s execution time. Share your understanding via GitHub and explain why we have used decorators and when we need to use them in your code as a comment..

import time

def timing_decorator(func):
    """
    This decorator measures how long a function takes to run.
    It records the start time before the function runs and the end time after it finishes,
    then prints the total execution time. We use decorators here to add this timing feature
    without changing the actual code of the function. Decorators are useful when we need
    to add common behavior (like logging, authentication, or timing) to multiple functions.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()        # record the start time
        result = func(*args, **kwargs)  # call the actual function
        end_time = time.time()          # record the end time
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to run.")
        return result
    return wrapper

@timing_decorator
def slow_function():
    print("Running a slow task...")
    time.sleep(2)  # simulate a time-consuming operation
    print("Task complete!")

# Example usage
slow_function()
