#  Password Generator (CLI)

A Python Command-Line Interface (CLI) application that generates secure and customizable passwords based on user preferences. The application allows users to choose password length, character types, and provides a password strength evaluation.

## Features

- Generate secure random passwords
- Multiple password modes
  - Recommended (12 characters)
  - Strong (16 characters)
  - Ultra Secure (20 characters)
  - Custom Length (8–50 characters)
- Include/Exclude:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Password strength analysis
- User-friendly CLI interface
- Input validation

## Technologies Used
- Python 3
- secrets
- random
- string

## Project Structure
```
.
├── modules/
│   ├── __init__.py
│   ├── generator.py
│   ├── menu.py
│   ├── strength.py
│   └── utils.py
├── assets/
├── docs/
├── main.py
├── requirements.txt
└── README.md
```

## How to Run

1. Clone the repository

```bash
git clone https://github.com/Harsh746-bit/synent-task4-passwordgenerator-harshbhanarkar.git
```

2. Open the project folder

```bash
cd synent-task4-passwordgenerator-harshbhanarkar
```

3. Run the application

```bash
python main.py
```

## Sample Output

```
Generated Password
-----------------------
M@7xLp!2Q#9k
Length : 12
Strength : Ultra Strong
```

## Internship

Developed as part of the **Synent Technologies Python Development Internship Program**.

## Developer

**Harsh Bhanarkar**
