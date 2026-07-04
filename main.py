from datetime import datetime

from modules.menu import (
    display_header,
    display_main_menu,
    display_password_menu,
    display_about,
    display_exit,
)

from modules.generator import generate_password
from modules.strength import check_password_strength
from modules.utils import get_yes_no, get_password_length


def generate():
    """Handle password generation."""

    while True:

        display_password_menu()

        while True:

            choice = input("\nSelect Password Mode: ").strip()

            if choice == "1":
                length = 12
                break

            elif choice == "2":
                length = 16
                break

            elif choice == "3":
                length = 20
                break

            elif choice == "4":
                length = get_password_length()
                break

            else:
                print("Invalid choice! Please try again.")

        print("\nSelect Character Types")

        include_upper = get_yes_no("Include Uppercase Letters? (Y/N): ")
        include_lower = get_yes_no("Include Lowercase Letters? (Y/N): ")
        include_numbers = get_yes_no("Include Numbers? (Y/N): ")
        include_special = get_yes_no("Include Special Characters? (Y/N): ")

        if not (
            include_upper
            or include_lower
            or include_numbers
            or include_special
        ):
            print("\nYou must select at least one character type.")
            continue

        password = generate_password(
            length,
            include_upper,
            include_lower,
            include_numbers,
            include_special,
        )

        strength = check_password_strength(password)

        generation_time = datetime.now().strftime("%d-%b-%Y %I:%M:%S %p")

        print("\n" + "=" * 60)
        print("                 GENERATED PASSWORD")
        print("=" * 60)

        print(f"\nPassword : {password}\n")

        print("=" * 60)
        print(f"Length              : {length}")
        print(f"Strength            : {strength}")
        print(f"Generated At        : {generation_time}")
        print(f"Uppercase Letters   : {'Yes' if include_upper else 'No'}")
        print(f"Lowercase Letters   : {'Yes' if include_lower else 'No'}")
        print(f"Numbers             : {'Yes' if include_numbers else 'No'}")
        print(f"Special Characters  : {'Yes' if include_special else 'No'}")
        print("=" * 60)

        print("\n1. Generate Another Password")
        print("2. Return to Main Menu")

        while True:

            option = input("\nEnter your choice: ").strip()

            if option == "1":
                break

            elif option == "2":
                return

            else:
                print("Invalid choice! Please enter 1 or 2.")


def main():
    """Application entry point."""

    while True:

        display_header()
        display_main_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            generate()

        elif choice == "2":
            display_about()
            input("\nPress Enter to continue...")

        elif choice == "3":
            display_exit()
            break

        else:
            print("\nInvalid choice! Please try again.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()