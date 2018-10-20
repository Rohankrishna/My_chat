import socket

host = 'localhost'
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
message = s.recv(1024)

while message:
    print("Message:",message.decode())
    message = s.recv(1024)

s.close()