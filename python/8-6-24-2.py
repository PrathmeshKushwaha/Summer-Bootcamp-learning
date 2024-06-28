# Definition of Exceptions and Basics of Exception Handling

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}. You can't divide by zero!")
        return None
    except TypeError as e:
        print(f"Error: {e}. Both inputs must be numbers!")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    else:
        print(f"The result is {result}")
        return result
    finally:
        print("Execution of divide function is complete.")

# Raising Exceptions and Exception Hierarchy
class CustomException(Exception):
    pass

def check_value(value):
    if value < 0:
        raise CustomException("Negative value error: Value cannot be negative!")
    else:
        print("Value is valid.")

# Testing divide function
print("Testing divide function:")
divide(10, 2)
divide(10, 0)
divide(10, 'a')
print("\nTesting check_value function:")
try:
        check_value(10)
        check_value(-5)
except CustomException as e:
        print(f"Caught custom exception: {e}")