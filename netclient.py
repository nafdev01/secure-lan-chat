import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# set the port number
port = 12345

# bind the socket to a public host, and a well-known port
client_socket.bind(("", port))

# set a timeout so the socket does not block indefinitely when trying to receive data
client_socket.settimeout(15)

# receive the broadcasted message
while True:
    try:
        data, address = client_socket.recvfrom(1024)
        print("Received message: %s" % data.decode("utf-8"))
    except socket.timeout:
        print("No more messages.")
        break

# close the socket
client_socket.close()
