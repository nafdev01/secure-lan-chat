# Secure Group Chat Application

This is a PyQt5 group chat application designed with a focus on security. It enforces 2FA at sign up and sign in, uses SSL encryption for database operations, and secures chat communication with AES and RSA. The application logs all user actions and uses a randomized salt for password storage. It also allows message storage and deletion. The application uses MariaDB for the database and communicates directly with the database for operations other than sending messages, which are sent using a socket server.

## Features

This PyQt5 group chat application is designed with a strong focus on security and user-friendly interface. Here are the key features:

### Two-Factor Authentication (2FA)
The application enforces 2FA both at the time of sign up and sign in. This means that users will need to provide two different types of identification to access their account, making it harder for unauthorized users to gain access.

### SSL Encryption for Database Operations
All database operations are secured with SSL encryption. This means that any data sent between the application and the database is encrypted, making it unreadable to anyone who might intercept it. This is crucial for protecting sensitive information like user credentials and chat messages.

### AES and RSA for Chat Communication
The application uses two different encryption algorithms to secure chat communication: AES (Advanced Encryption Standard) and RSA (Rivest–Shamir–Adleman). AES is used for encrypting the actual chat messages, while RSA is used for securely sharing the AES keys between users.

### User Action Logging
The application keeps a log of all user actions, including authentication actions and signing up. This can be useful for tracking user behavior, identifying potential security threats, and debugging issues.

### Randomized Salt for Password Storage
To protect user passwords, the application uses a technique called "salting". A random "salt" value is generated for each user and combined with their password before it's hashed and stored. This makes it much harder for attackers to use precomputed tables (like rainbow tables) to crack the passwords.

### Message Storage and Deletion
The application stores all chat messages, allowing users to view their chat history. Users also have the ability to delete their messages if they wish.

### MariaDB Database
The application uses MariaDB, a popular open-source relational database, for storing user data and chat messages. MariaDB is known for its speed and reliability, making it a great choice for this application.

### Direct Database Communication
For most operations, the application communicates directly with the database. This allows for efficient data retrieval and manipulation.

### Socket Server for Message Transmission
For sending messages, the application uses a socket server. This allows for real-time communication between users, as messages can be pushed to the recipient as soon as they're sent.

## Setup Instructions

1. **Create a Python virtual environment**:
    ```bash
    python3 -m venv env
    ```

2. **Enter the virtual environment**:
    ```bash
    source env/bin/activate
    ```

3. **Install requirements**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set the environment variables** in a `.env` file for `DB_USER`, `DB_PASSWORD`, `DB_NAME`, `DB_PORT`, `SERVER_HOST`, `SERVER_PORT`. If these are not set, the defaults will be used.

    Here are the default values:
    ```env
    DB_USER=secure_admin
    DB_PASSWORD=Annda8*j3s_Dje
    DB_NAME=secure_chat
    DB_PORT=3306
    SERVER_HOST="127.0.0.1"
    SERVER_PORT=3000
    ```

## Usage

After setting up the environment and installing the requirements, you can start the application by running the main script (replace `main.py` with the actual name of your script):

```bash
python main.py
