def log_decorator(func):
    """
    This decorator adds logging to a function.
    It prints the function name, its arguments, and the result
    each time the function is called. This helps track what the
    function is doing without changing its actual code.
    """
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

# Example: This will print what happens when add() is called
add(3, 5)
