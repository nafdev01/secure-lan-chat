import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get the local machine name
host = socket.gethostname()

# set the port number
port = 12345

# bind the socket to a public host, and a well-known port
server_socket.bind((host, port))

# broadcast a message
message = "Hello, everyone!"
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server_socket.sendto(message.encode("utf-8"), ("<broadcast>", port))

# close the socket
server_socket.close()
