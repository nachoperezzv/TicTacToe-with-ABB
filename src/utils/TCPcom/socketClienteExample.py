#!/usr/bin/env python

import socket

class SocketClient:

    """
    Destinada a la gestión simplificada de la comunicación desde la parte 
    cliente del Back-End
    
    """

    def __init__(self, host='localhost', port=4000):
        """
        Variables de instancia para el objeto

        params: 
            :host   :   anfitrión de la comunicación, por defecto el PC, local
            :port   :   puerto por el que se realiza, por defecto el 4000
        """

        self.host = host
        self.port = port
    
    
    def __connect(self):

        """
        Se crea el objeto socket necesario para la conexión y esta se realiza
        con el protocolo IPv4. Necesita una IP y un puerto. 

        Se instancia el cliente ya que el servidor no está abierto constantemente, 
        por lo que ha de ser un 'nuevo' cliente el que se conecte para enviar. 

        Las constantes con las que se instancia una conexión definen los protocolos: 
            AF_INET -> IPv4
            SOCK_STREAM -> TCP
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.sock.connect((self.host, self.port))

    

    def mysend(self, msg):

        """
        Método para el envío de mensajes. Internamente se encarga de abrir la conexión, 
        codificar el mensaje, enviarlo y recibir la comprobación de llegada. 

        Retorna un valor 'True' si el envío se ha realizado con éxito

        params: 
            :arg msg     : (str) cualquier cadena de texto a enviar por el socket
        """
        
        self.__connect()

        bmsg = bytes(msg, 'ascii')

        self.sock.send(bmsg)

        self.receive = self.myreceive()

        return True if self.receive != None else False
       
    
    def myreceive(self):

        """
        Recepción de mensajes, decodificación y retorno de una cadena de texto. 

        El mensaje de comprobación de un envío se almacena en 'self.receive', para 
        utilizar este método se debe tener otro mensaje enviado desde el servidor.

        El mensaje recibido por este método no se almacena en una variable de instancia, 
        solo se retorna
        """
        
        bmsg = self.sock.recv(1024)
    
        msg = str(bmsg, 'ascii')

        return msg


  
# Ejemplo de prueba: 
"""
host = "127.0.0.1"
port = 4000

client = SocketClient(host, port)
client.mysend("J1;C1")
rec = client.myreceive()
#print(rec)
"""


"""
i = 0
while i<3:
    
    msg = "Ir a A" + str(i)
    bool_receive = client.mysend(msg)
    rec = client.myreceive()
    print(rec)
    i = i+1
"""
