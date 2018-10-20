import socket                                                   #Importing socket 

host = 'localhost'                                              #Declaring hostname
port = 8080                                                     #Port number which is open
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           #Creating a socket at that port
s.connect((host, port))                                         #Connecting to that specific host name and port number
message = s.recv(1024)                                          #Receiving the message and we are telling thatthe message capacity can be 1024 bytes long

while message:
    print("Message:",message.decode())                          #while the message is TRUE (means if there exists a message, then decode that message and print it)
    message = s.recv(1024)                                      #receive the message

s.close()