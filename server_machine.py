import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5000))  # Listen on all interfaces
server_socket.listen(1)

print("Server listening...")

connection, client_address = server_socket.accept()
with connection:
    data = connection.recv(1024)

