"""
SecurePass CLI

Module: utils.py
Description:
Contains helper functions for user input and validation.
"""


def get_yes_no(prompt):
    """
    Get a valid Yes/No response from the user.
    """

    while True:
        choice = input(prompt).strip().lower()

        if choice in ("y", "yes"):
            return True

        if choice in ("n", "no"):
            return False

        print("Invalid input! Please enter Y or N.")


def get_password_length():
    """
    Ask the user for a custom password length.
    """

    while True:
        try:
            length = int(input("Enter password length (8-50): "))

            if 8 <= length <= 50:
                return length

            print("Password length must be between 8 and 50.")

        except ValueError:
            print("Please enter a valid number.")