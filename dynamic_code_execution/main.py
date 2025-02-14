# Dynamic Code Execution - Demonstrating exec and eval in Python

def demonstrate_exec():
    """
    Demonstrates the use of exec to execute a dynamically created function.
    
    This function defines a simple greeting function and executes it
    in a local scope, allowing for dynamic function creation and execution.
    """
    code = """def greet(name):
               return f"Hello, {name}\""""  # Code string defining a function to greet a user.
    
    # Executing the code string 
    local_scope = {}  # Dictionary to hold the local scope for the executed code.
    exec(code, {}, local_scope)  # Execute the code in an empty global scope and the local scope.
    print(local_scope["greet"]("Yared"))  # Call the dynamically created greet function.

demonstrate_exec()

def demonstrate_eval():
    """
    Demonstrates the use of eval to evaluate a string as a Python expression.
    
    This function prompts the user for an expression or function name,
    evaluates it, and prints the result.
    """
    expression = input("Type an expression or insert func name: - ")  # Prompt user for input.
    result = eval(expression)  # Evaluate the input expression.

    print(f"Result of eval is: {result}")  # Print the result of the evaluation.

def demonstrate_safe_eval():
    """
    Demonstrates a safer way to evaluate expressions using eval.
    
    This function restricts the evaluation context to a predefined set of variables,
    preventing access to global variables or functions, enhancing security.
    """
    # Define what the evaluation should have access to
    expression = input("Type an expression that uses a, b and c: ")  # Prompt user for input.
    values = {'a': 2, 'b': 1, 'c': 0}  # Define a dictionary of allowed variables.

    # Evaluate the expression with restricted access to prevent security issues.
    result = eval(expression, {}, values)  # Evaluate the expression with restricted access.
    print(f"Result of safe eval: {result}")  # Print the result of the safe evaluation.



