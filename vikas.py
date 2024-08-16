def arithmetic_operation(a, b, operation):
    """
    Perform arithmetic operations on two numbers.

    Parameters:
    a (float): The first number.
    b (float): The second number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    float: The result of the arithmetic operation.
    """
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

# Example usage:
result = arithmetic_operation(10, 5, 'add')
print(result)  # Output: 15
