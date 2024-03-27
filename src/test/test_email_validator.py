from src.validators.emailValidator import validate_email

def test_valid_email():
    """
    Validate if a valid email is correctly validated.

    Parameters:
    - None

    Returns:
    - None
    """
    assert validate_email('user@example.com') == True

def test_invalid_email():
    """
    Validate if an invalid email is correctly detected.

    Parameters:
    - None

    Returns:
    - None
    """
    assert validate_email('user.example.com') == False

def test_empty_email():
    """
    Validate if an empty string is considered an invalid email.

    Parameters:
    - None

    Returns:
    - None
    """
    assert validate_email('') == False

def test_email_without_at():
    """
    Validate if an email without the '@' character is considered invalid.

    Parameters:
    - None

    Returns:
    - None
    """
    assert validate_email('userexample.com') == False

def test_email_without_dot():
    """
    Validate if an email without the '.' character is considered invalid.

    Parameters:
    - None

    Returns:
    - None
    """
    assert validate_email('user@examplecom') == False