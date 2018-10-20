import socket                                                                       #Importing socket

host = 'localhost'                                                                  #Declaring hostname
port = 8080                                                                         #Port number which is open
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                               #Creating a socket at that port
s.bind((host,port))                                                                 #Binding together the host and port number and they are to be passed only as a tuple, it doesn't take two parameters
s.listen(1)                                                                         #Listening, and 1 means that it will listen to only 1 client
print("The server is now listening for a request on port:",port)                    
conn, address = s.accept()                                                          #The connection establishment and the address from which the connection has come from are here
print("Connection has been established from: ",str(address))
conn.send("\n Hello This is J.A.R.V.I.S  and I am running the server ".encode())    #Sending the connection establishment acknowledgement to the client
conn.close()                                                                        #Close the connection
