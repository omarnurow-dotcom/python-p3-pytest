# string_functions.py

def return_string():
    """
    This function returns a string.
    """
    return "Hello, World!"

def interpolate_string(base_string, insert_string):
    """
    This function takes two strings and inserts insert_string into base_string.
    
    Example:
    interpolate_string("I love {}", "Python") -> "I love Python"
    """
    return base_string.format(insert_string)

    