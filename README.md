# Secure Group LAN Chat Application

The Secure Group LAN Chat Application is a PyQt5-based group chat solution designed to facilitate secure real-time communication over local area networks (LAN). With a strong emphasis on security and user-friendly interface, this application offers a robust platform for organizations or groups to exchange messages confidentially within their network environment.


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


## Pre-requisites
1. **Python 3.10**: Ensure you have Python 3.10 or higher installed on your system. You can download the latest version of Python from the [official website](https://www.python.org/downloads/).
2. **PyQt5**: The application uses PyQt5 for the graphical user interface. You can install PyQt5 using pip:
    ```bash
    pip install PyQt5
    ```
3. **MARIA DB**: Our application uses MariaDB for database operations. You’ll need to have it installed and properly configured on your system. You can download MariaDB from the [official website](https://mariadb.org/download/).
4. **Google Authenticator**: To use the 2FA feature, you'll need to install the Google Authenticator app on your mobile device. You can download the app from the [Google Play Store](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2) or the [Apple App Store](https://apps.apple.com/us/app/google-authenticator/id388497605).
5. **OpenSSL**: To use SSL encryption for database communication, you'll need to have OpenSSL installed on your system. You can download OpenSSL from the [official website](https://www.openssl.org/source/).
6. **General Knowledge**: You should have a basic understanding of Python programming, PyQt5, MariaDB, and SSL encryption to work with this application.


## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/nafdev01/secure-lan-chat.git
    cd secure-lan-chat
    ```

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
5. **Configure SSL for Database Communication**
    
To enable SSL encryption for database communication, you need to generate SSL certificates and configure MariaDB to use them. [An example of how this on linux systems can be done can be found here](https://www.cyberciti.biz/faq/how-to-setup-mariadb-ssl-and-secure-connections-from-clients/). Here's a general outline of the steps involved:

- **Generate SSL Certificates**: You can generate SSL certificates using tools like OpenSSL. The certificates typically include a private key, a certificate signing request (CSR), and a certificate signed by a certificate authority (CA). Example of [how to do this](https://mariadb.com/docs/server/security/data-in-transit-encryption/create-self-signed-certificates-keys-openssl/)
- **Configure MariaDB**: Update the MariaDB configuration file (`my.cnf`) to specify the SSL certificates and enable SSL encryption. You'll need to set the `ssl-ca`, `ssl-cert`, and `ssl-key` options in the `[mysqld]` section of the configuration file. [Instructions](https://mariadb.com/kb/en/securing-connections-for-client-and-server/)
- **Restart MariaDB**: After configuring the SSL certificates, restart the MariaDB service to apply the changes.
- **Test SSL Connection**: You can test the SSL connection by connecting to the MariaDB server using the `mysql` command-line client with the `--ssl-ca`, `--ssl-cert`, and `--ssl-key` options.
- **Move SSL Certificates and Key**: Move the SSL certificates and key to the cert directory of your project with the names `ca-cert.pem`, `client-cert.pem`, and `client-key.pem`. `ca-cert.pem` will be the CA certificate, `client-cert.pem` will be the client certificate, and `client-key.pem` will be the client key.

##### *Note*:
  - Once you transfer the SSL files to `cert`, ensure that your current user has access to the files.
  - The steps for configuring SSL encryption for MariaDB may vary depending on your specific setup and requirements. It's important to follow the [official documentation and best practices for securing MariaDB database connections with SSL](https://mariadb.com/kb/en/securing-connections-for-client-and-server/).


## Usage

After setting up the environment and installing the requirements, you can start the application by running the main script (replace `main.py` with the actual name of your script):

```bash
python main.py
```

### 6. Troubleshooting:
In the event that users encounter issues during setup or usage of the Secure Group LAN Chat Application, here are some common troubleshooting steps and solutions:

- **Issue**: Unable to start the application due to missing dependencies.
  - **Solution**: Ensure all dependencies listed in the `requirements.txt` file are installed in your Python environment. Use `pip install -r requirements.txt` to install missing dependencies.

- **Issue**: Database connection error.
  - **Solution**: Check that MariaDB is running and accessible from your system. Verify that the database credentials and connection settings in the `.env` file are correct. Additionally, ensure that SSL encryption is configured correctly for database communication.

- **Issue**: 2FA code not working or authentication failure.
  - **Solution**: Double-check that the time on your device running the Google Authenticator app is synchronized correctly. If the time is not synchronized, the generated TOTP codes may be invalid. Reconfigure the 2FA setup and ensure the generated TOTP codes match the expected values.

- **Issue**: Application crashes or freezes during usage.
  - **Solution**: Check the application logs for any error messages or stack traces that may indicate the cause of the crash. Ensure that your system meets the minimum hardware requirements for running the application. If the issue persists, consider reaching out to the project maintainers for assistance.

For additional assistance or to report specific issues not covered here, please refer to the project's issue tracker on GitHub or reach out to the project maintainers directly.

### 7. Contributing:
Contributions to the Secure Group LAN Chat Application are welcome and encouraged! If you'd like to contribute to the project, please follow these guidelines:

- **Bug Reports**: If you encounter any bugs or unexpected behavior while using the application, please submit a detailed bug report on the project's issue tracker. Include steps to reproduce the issue and any relevant error messages or logs.

- **Feature Requests**: Have an idea for a new feature or improvement? Submit a feature request on the project's issue tracker, describing the proposed feature and its potential benefits to users.

- **Pull Requests**: To contribute code changes or enhancements to the project, please fork the repository, create a new branch for your changes, and submit a pull request against the main branch. Ensure your code changes adhere to the project's coding standards and include appropriate documentation and tests.

For more information on contributing to the project, please reach out to the project maintainers for guidance.