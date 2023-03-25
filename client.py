# Import necessary libraries
import socket
import threading

# Choose a nickname for the client
nickname = input("Choose your nickname: ")

# Create a client socket and connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55555))


# Function to receive messages from the server and send nickname if requested
def receive():
    while True:
        try:
            # Receive message from server
            message = client.recv(1024).decode("ascii")

            # If the message is a nickname request, send the chosen nickname to the server
            if message == "NICK":
                client.send(nickname.encode("ascii"))
            else:
                # Otherwise, print the received message
                print(message)

        except:
            # If an error occurs, close the connection and exit the loop
            print("An error occurred!")
            client.close()
            break


# Function to send messages to the server
def write():
    while True:
        # Prompt the user to input a message and send it to the server
        message = "{}: {}".format(nickname, input(""))
        client.send(message.encode("ascii"))


# Create two threads to run the receive() and write() functions concurrently
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
