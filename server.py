import socket
import threading

# Function to handle a client
def handle_client(client_socket):
    # Send a welcome message to the client
    client_socket.send("Welcome to the server!".encode())

    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Client says: {data}")

        # Send a response to the client
        response = input("Enter your response: ")  # Get response from the server user
        client_socket.send(response.encode())

    # Close the connection with the client
    client_socket.close()

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = '127.0.0.1'  # localhost
port = 12345
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen()

print(f"Server listening on {host}:{port}")

# List to store client sockets
clients = []

# Infinite loop to accept connections from clients
while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Add the new client socket to the list
    clients.append(client_socket)

    # Create a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
