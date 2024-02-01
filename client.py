import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = '127.0.0.1'  # localhost
port = 12345
client_socket.connect((host, port))

# Receive data from the server
data = client_socket.recv(1024).decode()
print(f"Server says: {data}")

# Send data to the server
message = "Hello, server! Thanks for having me."
client_socket.send(message.encode())

# Close the connection
client_socket.close()
