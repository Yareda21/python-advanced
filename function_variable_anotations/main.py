# Variable Annotations
name: str = "Yared"  # The name of the individual
age: int = 23        # The age of the individual
is_student: bool = True  # Indicates if the individual is a student

def calculator(num1: float, num2: float) -> float:
    """
    Calculate the sum of two floating-point numbers.

    Parameters:
    num1 (float): The first number to add.
    num2 (float): The second number to add.

    Returns:
    float: The sum of num1 and num2.
    """
    return num1 + num2

def greet(name: str) -> str:
    """
    Generate a greeting message for the given name.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}"

# Example usage of the calculator function
result = calculator(5.0, 3.0)  # Calculate the sum of 5.0 and 3.0
print(result)  # Output the result of the calculation

# Example usage of the greet function
greeting_message = greet(name)  # Generate a greeting for the individual
print(greeting_message)  # Output the greeting message