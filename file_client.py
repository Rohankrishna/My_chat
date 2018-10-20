import socket                                               #Importing socket 
host='localhost'                                            #Declaring hostname
port=8080                                                   #Port number which is open
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)         #Creating a socket at that port
s.connect((host, port))                                     #Connecting to that specific host name and port number
file_name=input("Enter file name you want:")                
print(file_name)
s.send(file_name.encode())                                  #Requesting the file name from which we want information from
read_file=s.recv(1024)                                      #Receiving the requested information from the server side
print(read_file.decode())                                   #The file information received is in encoded format, so decoding it and printing to normal form
s.close()
