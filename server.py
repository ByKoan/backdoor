from socket import socket
from time import sleep
#from sys import exit

try:


    s = socket() # crear una instancia socket
    s.bind(("127.0.0.1", 8000)) # poner a la escucha en 127.0.0.1:8000
    s.listen(1) # poner un maximo de 1 cliente
    print("El server esta a la escucha en 127.0.0.1:8000....")
    s, v = s.accept() # acepta conexiones, pasando a ser s un nuevo socket

    print(s.recv(1024).decode()) # recibe un objeto bytes al cliente

    while True: #Bucle while que se repite infinitamente
        comando = input("Introduce su comando aqui: ") #Poner el comando que haya introducido el usuario en la variable comando
        s.send(str(len(comando)).encode()) #Manda al cliente la longitud de el comando
    
        sleep(0.5) #Espera 0,5 segundos
        s.send(comando.encode()) #Manda al cliente el comando 
        
        if bool(s.recv(1024).decode()): #Comprueba si el mensaje recibido es un booleano
            sleep(0.5) #Espera 0,5 segundos
            
            #Si el mensaje recibido es "True":
            status_output_command = int(s.recv(1024).decode()) #Recibimos el estado de salida del comando en el cliente y lo guardamos en una variable
            if status_output_command == 0: #Comparamos la variable con 0 (Se ejecuto el comando)
                print(s.recv(1024).decode()) #Recibimos la salida del comando y lo imprimimos
            else:
                print("Comando no valido.")
        else:
            print("El cliente a muerto")
            break
        
    s.close() # cierra el socket
except KeyboardInterrupt:
    print("Saliendo del programa...")
