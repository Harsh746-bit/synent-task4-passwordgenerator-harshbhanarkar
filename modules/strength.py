"""
SecurePass CLI

Module: strength.py
Description:
Evaluates the strength of generated passwords.
"""

import string


def check_password_strength(password):
    """
    Evaluate the strength of the password.
    """

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak"

    elif score == 3:
        return "Medium"

    elif score == 4:
        return "Strong"

    return "Ultra Strong"