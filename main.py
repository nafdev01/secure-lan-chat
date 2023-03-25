import os
import socket
import threading

import rsa

choice = input("Do you want to host (1) or connect (2): ")
host = "10.1.47.27"

if choice == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, 9999))
    server.listen()

    client, _ = server.accept()

elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 9999))
else:
    exit()


def sending_messages(c):
    while True:
        message = input("")
        c.send(message.encode())
        print("You: " + message)


def receiving_messages(c):
    while True:
        message = c.recv(1024).decode()
        if message:
            print("Partner:" + message)


threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()
