
def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs a basic arithmetic operation between num1 and num2.
    Supported operations: add, subtract, multiply, divide.
    """

    operation = operation.strip().lower()

    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2

    else:
        return "Error: Invalid operation"
