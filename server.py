import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = '127.0.0.1'  # localhost
port = 12345
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen()

print(f"Server listening on {host}:{port}")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

# Send data to the client
message = "Hello, client! Welcome to the server."
client_socket.send(message.encode())

# Receive data from the client
data = client_socket.recv(1024).decode()
print(f"Client sent: {data}")

# Close the connection
client_socket.close()
server_socket.close()
