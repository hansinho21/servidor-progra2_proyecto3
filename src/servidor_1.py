# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import json
import random
import socket
import threading
    # Import socket module
print("pasa por aqui")
answers = {}
threads = []
#read = json.loads(open('preguntas.json').read())
#a = read
#for counter in range(len(a)):
#    answers[read[counter]['enunciado']] = [read[counter]['respuestas']]

def teams(conn):
    m = '{"mensaje": conexión, "valor": "Ingrese el nombre del equipo"}'
    msg = conn.recv(1024) #Resivir mensaje del cliente
    print msg
    jsonObj = json.loads(m)
    conn.send(jsonObj)
    print("nuevo hilo/cliente")
    
soc = socket.socket()         # Create a socket object
host = "localhost" # Get local machine name
port = 8000                # Reserve a port for your service.
soc.bind(("192.168.1.4", port))       # Bind to the port
soc.listen(5) 
# Now wait for client connection.
t = threading.Thread(target=acceptConnections)
t.start()

while(true):
    flag = input("Comenzar fase de preguntas")
    if(flag == "si"):
        t.join()
        break

def acceptConnections():
    while True:
        conn, addr = soc.accept()     # Establish connection with client.
        print ("Got connection from", addr)
        t = threading.Thread(target=teams, args=(conn, addr))
        threads.append(t)
        t.start()

    
    


    