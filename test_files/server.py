# Import necessary libraries
import socket
import threading

# Set the IP address and port number for the server
host = "127.0.0.1"
port = 55555

# Create a server socket, bind it to the IP address and port number, and start listening for connections
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Create empty lists to store the clients and their nicknames
clients = []
nicknames = []


# Function to broadcast a message to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)


# Function to handle messages from a single client
def handle(client):
    while True:
        try:
            # Receive a message from the client and broadcast it to all other clients
            message = client.recv(1024)
            broadcast(message)
        except:
            # If an error occurs, remove the client from the clients list and the corresponding nickname from the nicknames list, close the connection, and broadcast a message indicating that the client has left
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast("{} left!".format(nickname).encode("ascii"))
            break


# Function to receive connections from clients and handle their messages
def receive():
    while True:
        # Accept a new connection from a client
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request and store the client's nickname
        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)

        # Print and broadcast the client's nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode("ascii"))
        client.send("Connected to server!".encode("ascii"))

        # Start a new thread to handle messages from the connected client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


# Call the receive() function to start accepting connections and handling messages
receive()
