from custom import ValidationError
from logger import getFullPatch

import socket, sys, os, traceback, logging

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
logging.basicConfig(
    filename=f'{getFullPatch()}/log/logger.log',
    filemode='a',
    level=logging.INFO,
    encoding='utf-8', 
    format='%(asctime)s - %(levelname)s:%(filename)s:%(message)s',
    datefmt='%d/%m/%Y;%H:%M:%S'
)

class TCP:
    """
    Destinada a la gestión simplificada de la comunicación desde la parte 
    cliente del Back-End
    
    """

    def __init__(self, host='172.20.10.120', port=4000):
        """
        Variables de instancia para el objeto

        params: 
            :host   :   anfitrión de la comunicación, por defecto el PC, local
            :port   :   puerto por el que se realiza, por defecto el 4000
        """

        self.__host = host
        self.__port = port
    
    def set_port(self, port):
        self.__port = port

    def set_host(self, host): 
        self.__host = host
 
    def mysend(self, msg):

        """
        Método para el envío de mensajes. Internamente se encarga de abrir la conexión, 
        codificar el mensaje, enviarlo y recibir la comprobación de llegada. 

        Retorna un valor 'True' si el envío se ha realizado con éxito

        params: 
            :arg msg     : (str) cualquier cadena de texto a enviar por el socket
        """
        try:
            self.__connect()
            # bmsg = bytes(msg, 'ascii')
            self.sock.send(self.__to_bytes(msg))
            self.receive = self.__myreceive()

            return True if self.receive != None else False
    
        except ValidationError as e:
            logging.error(str(e), traceback.format_exc())
        
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
        
        self.sock.connect((self.__host, self.__port))

    def __myreceive(self):

        """
        Recepción de mensajes, decodificación y retorno de una cadena de texto. 

        El mensaje de comprobación de un envío se almacena en 'self.receive', para 
        utilizar este método se debe tener otro mensaje enviado desde el servidor.

        El mensaje recibido por este método no se almacena en una variable de instancia, 
        solo se retorna
        """
        try: 
            bmsg = self.sock.recv(1024)
            msg = str(bmsg, 'ascii')

            return msg

        except ValidationError as e:
            logging.error(str(e), traceback.format_exc())

    def __to_bytes(self, msg):
        return bytes(msg, 'ascii')
    
    
  
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
