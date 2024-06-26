import argparse
import datetime
import json
import os
import random
import socket
import string
import threading
from base64 import b64decode, b64encode

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from termcolor import colored


class Client:
    def __init__(self):
        self.server = "192.168.241.103"
        self.port = 8394
        self.username = self.get_username()
        self.key_pairs = self.create_key_pairs()

    ###### set the username
    def get_username(self):
        username = input("Enter your username: ")
        return username

    ###### Create the connection to the server
    def create_connection(self):
        ###### Setting up the socket, takes the serverIP and portNumber arguments to set up the connection to the server
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((self.server, self.port))
        except Exception as e:
            print(colored("[!] " + e, "red"))

        ####### Initial message exchanges for the communication
        ####### Setting up username, keys
        ####### Calling exchange secret and pub key functions

        self.s.send(
            self.username.encode()
        )  # Inform the server about the username connected
        print(colored("[+] Connected successfully", "yellow"))
        print(colored("[+] Exchanging keys", "yellow"))

        self.create_key_pairs()  # Create key pairs
        self.exchange_public_keys()  # Initial public key exchange
        global secret_key  # Global variable to hold the secret key for AES encryption
        secret_key = (
            self.handle_secret()
        )  # Function to get the secret generated by the server

        print(colored("[+] Initial set up had been completed!", "yellow"))
        print(colored("[+] Now you can start to exchange messages", "yellow"))

        ####### InputHandle for sending messages and MessageHandle thread for receiving messages
        message_handler = threading.Thread(target=self.handle_messages, args=())
        message_handler.start()
        input_handler = threading.Thread(target=self.input_handler, args=())
        input_handler.start()

    ####### Handle receiving messages
    def handle_messages(self):
        while True:
            message = self.s.recv(1024).decode()
            if message:
                key = secret_key  # The secret key to use for AES decryption
                decrypt_message = json.loads(message)  # Load the json formatted message
                iv = b64decode(
                    decrypt_message["iv"]
                )  # Take out the initialization vector and b64 decode it
                cipherText = b64decode(
                    decrypt_message["ciphertext"]
                )  # Take out the ciphertext and b64 decode it
                cipher = AES.new(
                    key, AES.MODE_CFB, iv=iv
                )  # Create and AES object, parameters: [secret_key], [counter feedback mode], [initialization vector]
                msg = cipher.decrypt(
                    cipherText
                )  # Use the object to decrypt the ciphertext
                current_time = datetime.datetime.now()
                print(
                    colored(
                        current_time.strftime("%Y-%m-%d %H:%M:%S ") + msg.decode(),
                        "green",
                    )
                )  # It produces a byte encoded output so you have to decode it to display as string
            else:
                print(colored("[!] Lost the connection to the server", "red"))
                print(colored("[!] Closing down the connection", "red"))
                self.s.shutdown(socket.SHUT_RDWR)
                os._exit(0)

    ####### Handle user input and send message
    def input_handler(self):
        while True:
            message = input()  # Take the input from the user
            if message == "EXIT":  # EXIT will close down the client
                break
            else:
                key = secret_key
                cipher = AES.new(
                    key, AES.MODE_CFB
                )  # Initialize AES object for encryption, parameters: [key], [counter feedback mode]
                message_to_encrypt = (
                    self.username + ": " + message
                )  # The message what will be sent, containing the username and the user input
                msgBytes = (
                    message_to_encrypt.encode()
                )  # Byte encode it, because AES input must be byte encoded
                encrypted_message = cipher.encrypt(msgBytes)  # Encrypt the message
                iv = b64encode(cipher.iv).decode(
                    "utf-8"
                )  # Generate the initialization vector, b64encode it, than utf-8 representation to send
                message = b64encode(encrypted_message).decode(
                    "utf-8"
                )  # Same process to the encrypted message, to overcome special chars
                result = json.dumps(
                    {"iv": iv, "ciphertext": message}
                )  # Insert it into a json dictionary
                self.s.send(result.encode())  # Send it in byte encoded form

        self.s.shutdown(socket.SHUT_RDWR)
        os._exit(0)

    ###### Receiving the secret key for symmetric encryption

    ###### Receiving the secret key for symmetric encryption
    def handle_secret(self):
        secret_key = self.s.recv(
            1024
        )  # The secret key coming from the server, and used for encryption and decryption
        private_key = RSA.importKey(
            self.key_pairs["private"]
        )  # Import the client private key to decrypt the secret
        cipher = PKCS1_OAEP.new(
            private_key
        )  # Using the client private key to decrypt the secret
        return cipher.decrypt(secret_key)

    ###### Send the public key to the server to encrypt the secret
    ###### The secret is generated by the server and used for symmetric encryption
    def exchange_public_keys(self):
        try:
            print(colored("[+] Getting public key from the server", "blue"))
            server_public_key = self.s.recv(1024).decode()
            server_public_key = RSA.importKey(server_public_key)

            print(colored("[+] Sending public key to server", "blue"))
            public_pem_key = RSA.importKey(self.key_pairs["public"])
            self.s.send(public_pem_key.exportKey())
            print(colored("[+] Exchange completed!", "yellow"))

        except Exception as e:
            print(colored("[!] ERROR, you messed up something.... " + e, "red"))

    ###### Generate public and private key pairs
    def create_key_pairs(self):
        try:
            private_key = RSA.generate(2048)
            public_key = private_key.publickey()
            private_pem = private_key.exportKey().decode()
            public_pem = public_key.exportKey().decode()
            keys = {"private": private_pem, "public": public_pem}
            return keys

        except Exception as e:
            print(colored("[!] ERROR, something went wrong: " + str(e), "red"))
            return None


if __name__ == "__main__":
    client = Client()
    client.create_connection()
