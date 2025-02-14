def my_decorator(func):
    """
    A decorator that wraps a function to print messages before and after its execution.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The wrapped function with added behavior.
    """
    def wrapper(*args, **kwargs):
        print(f"Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result
    

    return wrapper



@my_decorator
def say_hello(name: str) -> None:
    """
    Prints a greeting message.

    Args:
        name (str): The name of the person to greet.
    """
    print(f"Hello, {name}!")
