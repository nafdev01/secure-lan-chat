import socket
import hmac
import hashlib


# Set up the secret key to be used for HMAC
SECRET_KEY = b"secret_key"


def make_discoverable():
    UDP_IP = "0.0.0.0"
    UDP_PORT = 5030
    MESSAGE = b"I am the server!"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        hmac_message = hmac.new(SECRET_KEY, MESSAGE, hashlib.sha256).digest()
        sock.sendto(hmac_message + MESSAGE, ("<broadcast>", UDP_PORT))
        print("broadcasting...")


make_discoverable()
