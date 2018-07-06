# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import json
import random
import socket
import threading
 

threads = []
connections = []
admitConections = True
cantPreguntas = 10
answers = []
questions = {}
questionsList = []
currentQuestion = ""
leer = json.loads(open('preguntas.json').read())
for counter in range(len(leer)):
    questions[leer[counter]['enunciado']] = [leer[counter]['respuestas']]
    questionsList.append(leer[counter]['enunciado'])
#
    

    
def teams(conn):
    for counter in range(cantPreguntas):
        #recibe 1 respuesta por cliente 
        data = conn.recv(1024)
        print(data)
        a = False
        #revisar y guardar respuesta (enviarATodos)
        for counter in questions:
            if(counter == currentQuestion):
                for temp in questions[counter]:
                    if(temp == data):
                        a=True
        m = {"mensaje": "Recursos Python", "valor": "recursospython.com"}
        jsonObj = json.dumps(m)
        conn.send(jsonObj)                
    
#    print("nuevo hilo/cliente")
#    conn.send("Fase de preguntas")
#    m = '{"sitio": "Recursos Python", "url": "recursospython.com"}'
#    jsonObj = json.dumps(m)
#    conn.send(jsonObj)
       

def acceptConnections():
    while (admitConections):
        conn, addr = soc.accept()     # Establish connection with client.
        print ("Got connection from", addr)
        t = threading.Thread(target=teams, args=(conn,))
        threads.append(t)
        connections.append(conn)
       
        
soc = socket.socket()         # Create a socket object
host = "127.0.0.1" # Get local machine name
port = 8000               # Reserve a port for your service.
soc.bind((host, port))       # Bind to the port
soc.listen(5)  


th = threading.Thread(target=acceptConnections)
th.start()

while True:
    opcion = raw_input("Fase de preguntas")
    if(opcion == "si"):
        admitConections = False
        print admitConections
        break
        
for thread in threads:
    thread.start()
    
def enviarATodos(mensaje):
    for c in connections:
        c.send(mensaje)
def getRandom():
    return random.randint(1, len(leer)-1)

while True:
    print("enviando pregunta xD...")
    currentQuestion = questionsList[getRandom()]
    data = {"pregunta": "pregunta", "valor": currentQuestion}
    jsonObj = json.dumps(data)
    enviarATodos(jsonObj)
    response = raw_input("seguir")
    if(response == "si"):
        pass
    else:
        break
        
        
        
