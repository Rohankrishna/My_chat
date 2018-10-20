import socket                                                      #Importing socket 

host='localhost'                                                   #Declaring hostname
port=8080                                                          #Port number which is open

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)                #Creating a socket at that port
s.bind((host,port))                                                #Binding together the host and port number and they are to be passed only as a tuple, it doesn't take two parameters
s.listen(1)                                                        #Listening, and 1 means that it will listen to only 1 client
print("The server is listening on port: ",port)
conn, addr = s.accept()                                            #The connection establishment and the address from which the connection has come from are here
print("Connection has been established from", str(addr))
try:
    file_name=conn.recv((1024))                                    #The file name which is to be looked for is here
    file=open(file_name,'rb')                                      #Reading the file in binary format
    read_file=file.read()
    conn.send(read_file)                                           #Sending the read file
    file.close()
    conn.close()
except:
    conn.send("The requested file not found".encode())             #If the requested file doesn't exist the this message will be sent to the client