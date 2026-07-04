"""
SecurePass CLI

Module: menu.py
Description:
Contains functions related to displaying the user interface.
"""

def display_password_menu():
    """Display password generation options."""

    print("\nChoose Password Mode")
    print("-" * 30)
    print("1. Recommended (12 Characters)")
    print("2. Strong (16 Characters)")
    print("3. Ultra Secure (20 Characters)")
    print("4. Custom Length")

def display_header():
    """Display the application header."""

    print("\n" + "=" * 60)
    print("                 SECUREPASS CLI")
    print("=" * 60)
    print("     Professional Password Generator")
    # print("     Synent Technologies Internship")
    print("=" * 60)


def display_main_menu():
    """Display the main menu."""

    print("\nMain Menu")
    print("-" * 25)
    print("1. Generate Password")
    print("2. About")
    print("3. Exit")


def display_about():
    """Display project information."""

    print("\n" + "=" * 60)
    print("ABOUT PROJECT")
    print("=" * 60)
    print("Project      : SecurePass CLI")
    print("Developer    : Harsh Bhanarkar")
    print("Language     : Python 3")
    print("Interface    : Command Line (CLI)")
    print("Version      : 1.0")
    print("Internship   : Synent Technologies")
    print("=" * 60)

def display_exit():
    """Display exit message."""

    print("\n" + "=" * 60)
    print("Thank you for using SecurePass CLI.")
    print("Stay Secure! ")
    print("=" * 60)