import socket

client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
client_socket.connect('/tmp/uds_socket')

client_socket.sendall(b'Hello from client')
client_socket.close()
