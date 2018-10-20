import socket

host = 'localhost'
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       #
s.bind((host,port))
s.listen(1)
print("The server is now listening for a request on port:",port)
conn, address = s.accept()
#print(str(conn))
print("Connection has been established from: ",str(address))
conn.send("\n Hello This is J.A.R.V.I.S  and I am running the server ".encode())
conn.close()
