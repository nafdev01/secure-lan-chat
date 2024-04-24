# Secure Group Chat Application

This is a PyQt5 group chat application designed with a focus on security. It enforces 2FA at sign up and sign in, uses SSL encryption for database operations, and secures chat communication with AES and RSA. The application logs all user actions and uses a randomized salt for password storage. It also allows message storage and deletion. The application uses MariaDB for the database and communicates directly with the database for operations other than sending messages, which are sent using a socket server.

## Features

This PyQt5 group chat application is designed with a strong focus on security and user-friendly interface. Here are the key features:

#### 1. Two-Factor Authentication (2FA)

The application enforces 2FA at sign in. Users are required to provide two different types of identification to access their account:

- **Password**: Users must provide their password as the first factor of authentication. The password follows the default password policy, which requires a minimum of 8 characters, including at least one uppercase letter, one lowercase letter, one number, and one special character.
- **Google Authenticator**: The second factor of authentication involves using the Google Authenticator app, which generates a time-based one-time password (TOTP) for additional verification. The 2FA code is registered at sign up and is required at sign in.

This dual authentication process enhances the security of user accounts by adding an extra layer of protection against unauthorized access.
#### 2. SSL Encryption for Database Operations
The application uses MariaDB as its database. To secure database operations, the application uses SSL encryption. This ensures that data transmitted between the application and the database is encrypted and secure. SSL encryption helps protect sensitive information, such as user credentials and chat messages, from being intercepted.

#### 3. AES and RSA for Chat Communication
For sending messages, the application uses a socket server. This allows for real-time communication between users, as messages can be pushed to the recipient as soon as they're sent. The application uses two different encryption algorithms to secure chat communication: AES (Advanced Encryption Standard) and RSA (Rivest–Shamir–Adleman). AES is used for encrypting the actual chat messages, while RSA is used for securely sharing the AES keys between users (digital envelope).

#### 4. User Action Logging
The application keeps a log of all user actions, such as sign-ins, sign-outs, and message sends. This log helps track user activity and provides an audit trail for security purposes. By logging user actions, the application can detect and investigate any suspicious or unauthorized activities.

#### 5. Randomized Salt for Password Storage
To protect user passwords, the application uses a technique called "salting". A random "salt" value is generated for each user and combined with their password before it's hashed and stored. This adds an extra layer of security to the password storage process, making it more difficult for attackers to crack passwords using common techniques like rainbow tables or password lists.

#### 6. Message Storage and Deletion
The application stores all chat messages, allowing users to view their message history. Users can also delete messages, removing them from the chat history. This feature gives users control over their chat data and privacy, allowing them to manage their messages as needed.

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
5. Create and store the SSL certificates in the `cert` directory. The certificates should be named `server.crt` and `server.key`.

## Usage

After setting up the environment and installing the requirements, you can start the application by running the main script (replace `main.py` with the actual name of your script):

```bash
python main.py
