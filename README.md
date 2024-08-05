# Password Manager

Password Manager is a Python command line based application that helps you securely store and manage your passwords. It uses `sqlite3` for database management. 

## Getting Started

To get started with the Password Manager, follow these steps:

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/password-manager.git
    cd password-manager
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. First, run the `LoginCredDB` script to set up the database:

    ```bash
    LoginCredDB.py
    ```

2. Then, you can run the main application:

    ```bash
     main.py
    ```

### Symbols for Decoration

The `symbols.txt` file contains symbols used for decoration within the application. Ensure this file is in the same directory as your scripts.

## Usage

- Store new passwords
- Retrieve stored passwords
- Delete old passwords
- Update existing passwords

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request


---

*Happy password managing!*
