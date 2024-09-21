import string
from password.new_password import generate_password

def test_password_characters():
    """tests that generated password only contains valid characters"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # generating a longer password for valid test
    for char in password:
        assert char in valid_characters


def test_length_password():
    """test that checks if passworg length is equal to required length"""
    password = generate_password(12)
    assert len(password) == 12

def test_different_password():
    """test that checks if two generated passwords are different"""
    password1 = generate_password(12)
    password2 = generate_password(12)
    assert password1 != password2
