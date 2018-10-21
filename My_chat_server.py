import socket
from threading import Thread

clients={}
addresses={}

host='127.0.0.1'
port=8080

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))


def accept_client_connections():
    while True:
        client_conn, client_address = s.accept()
        print(str(client_address), "has connected")
        client_conn.send("Welcome to the chat room!! WHat's your name dude!?".encode("utf8"))
        addresses[client_conn]=client_address
        Thread(target=handle_client, args=(client_con, client_address)).start()


def broadcast(msg,prefix=""):
    for x in clients:
        x.send(bytes(prefix, "utf8")+msg)




def handle_client(conn, addr):
    name=conn.recv(1024).decode("utf8")
    welcome= "Welcome"+name+"Now you can start chattimg here. When you want to exit, type #quit to exit the chat room"
    conn.send(bytes(welcome,"utf8"))
    msg = name+"has joined the chat room"
    broadcast(bytes(msg,"utf8"))
    clients[conn]=name

    while True:
        msg = conn.recv(1024)

        if msg!=bytes("#quit","utf8"):
            broadcast(msg,name+":")

        else:
            conn.send(bytes("#quit","utf8"))
            conn.close()
            del clients[conn]
            broadcast(bytes(name+"has left the chat room"))







if __name__ == "__main__":
    number_of_clients=int(input("Enter number of people you want to allow in the cheta room: "))
    s.listen(number_of_clients)
    print("The server has started and is now listening ot the client requests.")
    t1=Thread(target=accept_client_connections)
    t1.start()                                                                                      #This will start the execution of a new thread
    t1.join()                                                                                       #Join() will stop the execution of current thread when a new thread joins and allows it to execute.


