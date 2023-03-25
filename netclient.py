import socket
import hmac
import hashlib


# Set up the secret key to be used for HMAC
SECRET_KEY = b"secret_key"


def discover_server():
    UDP_IP = "<broadcast>"
    UDP_PORT = 5030
    MESSAGE = b"I am the server!"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind(("0.0.0.0", UDP_PORT))

    server_found = False

    while not server_found:
        print("Searching...")
        hmac_message = hmac.new(SECRET_KEY, MESSAGE, hashlib.sha256).digest()
        sock.sendto(hmac_message + MESSAGE, (UDP_IP, UDP_PORT))
        sock.settimeout(5.0)
        try:
            data, addr = sock.recvfrom(1024)
            received_hmac_message = data[:32]
            received_message = data[32:]
            if hmac.compare_digest(hmac_message, received_hmac_message):
                print("Device found at", addr)
                server_found = True
                return True
            else:
                print("Invalid HMAC")
        except socket.timeout:
            print("No devices found.")


discover_server()
