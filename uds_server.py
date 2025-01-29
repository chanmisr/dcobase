import socket
import os

server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = '/tmp/uds_socket'

# Remove the socket if it already exists
if os.path.exists(server_address):
    os.unlink(server_address)

server_socket.bind(server_address)
server_socket.listen(1)

print("Server listening...")

connection, _ = server_socket.accept()
data = connection.recv(1024)
print("Received:", data.decode())

connection.close()
