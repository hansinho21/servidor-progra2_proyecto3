# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


import socket
    # Import socket module

soc = socket.socket()         # Create a socket object
host = "localhost" # Get local machine name
port = 2004                # Reserve a port for your service.
soc.bind((host, port))       # Bind to the port
soc.listen(5)                 # Now wait for client connection.
while True:
    conn, addr = soc.accept()     # Establish connection with client.
    print ("Got connection from", addr)
    msg = conn.recv(1024) #Resivir mensaje del cliente
    print (msg)
    if (msg == "Hello"):
        print("Hii everyone")
    else:
        print("Go away")
