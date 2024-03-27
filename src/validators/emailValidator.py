import re

def validate_email(email: str) -> bool:
    """
    Validate if the given string is a valid email address.

    Parameters:
    - email (str): The email address to be validated.

    Returns:
    - bool: True if the email is valid, False otherwise.
    """
    # regular expression to validate email
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    is_match = re.match(pattern, email)
    return bool(is_match)