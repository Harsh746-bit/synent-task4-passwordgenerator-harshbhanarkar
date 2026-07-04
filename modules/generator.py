"""
SecurePass CLI

Module: generator.py
Description:
Contains functions for generating secure passwords.
"""

import secrets
import random
import string

SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{}:;,.?"


def get_character_pool(
    include_upper,
    include_lower,
    include_numbers,
    include_special,
):
    """
    Create a character pool based on user preferences.
    """

    pool = ""
    guaranteed_characters = []

    if include_upper:
        pool += string.ascii_uppercase
        guaranteed_characters.append(
            secrets.choice(string.ascii_uppercase)
        )

    if include_lower:
        pool += string.ascii_lowercase
        guaranteed_characters.append(
            secrets.choice(string.ascii_lowercase)
        )

    if include_numbers:
        pool += string.digits
        guaranteed_characters.append(
            secrets.choice(string.digits)
        )

    if include_special:
        pool += SPECIAL_CHARACTERS
        guaranteed_characters.append(
            secrets.choice(SPECIAL_CHARACTERS)
        )

    return pool, guaranteed_characters


def generate_password(
    length,
    include_upper,
    include_lower,
    include_numbers,
    include_special,
):
    """
    Generate a secure password.
    """

    pool, password = get_character_pool(
        include_upper,
        include_lower,
        include_numbers,
        include_special,
    )

    if not pool:
        return None

    while len(password) < length:
        password.append(secrets.choice(pool))

    random.shuffle(password)

    return "".join(password)