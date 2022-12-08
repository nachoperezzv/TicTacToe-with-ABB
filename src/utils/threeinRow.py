from turtle import pos
from tablero import Tablero
from TCPcom.socketClienteExample import SocketClient
import random 
import time
import platform
import socket
from os import system

"""
COMBINAR EN ESTA CLASE SOLO LA LÓGICA DEL 3 EN RAYA
"""

def clear_window(): 
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

class ThreeInRow: 
    """
    Lógica de juego para el 3 en línea
    
    """

    def __init__(self) -> None:
        
        """
            Inicialización de un tablero para jugar al 3 en raya, este contiene 2 jugadores.
            Definición de las posibilidades de victoria (línea en filas o columnas y en diagonales)
        """
        
        self.__board = Tablero()
        
        self.__win_possibilities = {"line": ["A", "B", "C", "1", "2", "3"],
                     "diagonal": {"d1": ["A1", "B2", "C3"], "d2":["A3", "B2", "C1"]}}

    def __evaluate(self):
        """
        Utilizada para evaluar la heurística del estado en el que se encuentre
        la predicción. 

        Si gana la máquina la evaluación es positiva para ese tablero, si gana 
        el usuario es negativa, si no hay ganador aún es neutral
        """

        if self.isWinner(1): 
            return -1
        elif self.isWinner(2): 
            return 1
        else:
            return 0 

    def __minimax(self, depth, isCpu): 
        """
        Heurística para llegar al movimiento óptimo
        """

        # Si se quiere maximizar el movimiento, se tiene que poner 
        # un valor ínfimo (caso para la máquina)
        if isCpu:
            best = [None, -1000] 
            player = 2
        # Para las suposiciones del usuario es lo contrario
        else: 
            best = [None, 1000]
            player = 1 

        if depth == 0 or self.game_over():
            score = self.__evaluate()
            return [None,score]

        for cell in self.__board.empty_cells():
            self.__board.update_position(player, cell, isMove=False)
            score = self.__minimax(depth-1, not isCpu)
            self.__board.clear_position(cell)
            score[0] = cell

            if isCpu: 
                if score[1] > best[1]: 
                    best = score        # Máximo valor para la CPU
            else: 
                if score[1] < best[1]:
                    best = score        # Mínimo valor para el usuario
        
        return best

    def isWinner(self, player):

        """
        Comprueba si el jugador es ganador. 
        Se revisa si los tokens de este se encuentran en una de las dos diagonales. 
        También si se encuentran en la misma fila o columna

        params: 
            :arg player: (int) 1 or 2
        """

        winner = False

        values = self.__board.get_player_values(player)    

        # Comprobación de diagonales para los tokens del jugador
        if  ("a1" in values and "b2" in values and "c3" in values) or \
            ("a3" in values and "b2" in values and "c1" in values):
            winner = True

        # Si no es ganador aún, comprobación de filas y columnas
        if not winner: 
            for l in self.__win_possibilities["line"]:
                inLine = 0
                for v in values:
                    if v != None:
                        if l in v: 
                            inLine += 1                   

                    if inLine == 3:
                        winner = True
                        break
                
        return winner

    def game_over(self):
        """
        Comprueba si la partida ha terminado porque se tiene un ganador. 

        Devuelve quién ha ganado, en caso de que siga en juego 'False'.
        """

        return self.isWinner(1) or self.isWinner(2)

    def player_move(self, pos, player=1) -> bool: 
        """
        Mueve la ficha de un jugador a una posición concreta. 

        Internamente el método 'update_position' del tablero comprueba si se puede 
        realizar el movimiento y si es así, actualiza la posición del token. 

        Por defecto si mueve una ficha del usuario

        """

        possible = self.__board.update_position(player,pos,isMove=True)
        TCP_code = ""
        if possible:
            TCP_code = self.codify_tcp_message(player,pos)

        return possible, TCP_code


    def codify_tcp_message(self, player, pos):
        tcp_message = ""
        player_cod = "J" if player==1 else "Q"
        
        current_token = 0
        current_token = self.__board.get_current_token(player)
        
        # Se codifica mensaje
        tcp_message = tcp_message + player_cod + str(current_token) + ";" + pos
        
        return tcp_message


    def cpu_random_move(self, player = 2): 
        """
        Se mueve una ficha aleatoria a una posición aletoria que esté libre
        
        params
            :arg player: (int) Default 2nd player, cpu
        """

        occupied = True
        while occupied: 
            pos, occupied = random.choice(list(self.__board.get_board().items()))

        _, TCP_code = self.player_move(pos, player)

        return TCP_code

    def cpu_move(self, player=2):
        """
        Se mueve una ficha de la cpu con 'inteligencia' a una posición si la partida 
        no ha terminado.  

        """

        # Hay un ganador o el tablero está lleno
        if self.game_over() or self.__board.full_board():
            print("Win: {} o full: {}".format(self.game_over(), self.__board.full_board()))
            return False

        # Si está vacío se escoge una casilla aleatoria, sino se llama al minimax
        TCP_code = ""
        if self.__board.empty_board():
            TCP_code = self.cpu_random_move()
        else: 
            depth = len(self.__board.empty_cells())
            pos,_ = self.__minimax(depth, isCpu=True)
            
            print("Movimiento  CPU: " + str(pos) + "\n")
            _, TCP_code = self.player_move(pos, player)

        return TCP_code

    def show_board(self): 
        """
        Muestra el tablero
        """
        #clear_window()
        self.__board.print_board()

    def get_board(self):
        return self.__board.get_board()

# ____________________________ USE EXAMPLE ________________________________________

game = ThreeInRow()
""" Descomentar para probar conexion TCP"""
TCPclient = SocketClient("127.0.0.1",4000)

while not game.game_over():

    # Espera movimiento de jugador
    moved = False
    while not moved:
        move = str(input('Use [A1,..,C3]: '))
        moved, TCP_code_1 = game.player_move(move)

    # Se codifica mensaje de jugador
    print("TCP sent: " + TCP_code_1)
    """ Descomentar si se quiere probar conexion TCP-IP """
    TCPclient.mysend(TCP_code_1)

    # Se muestra tablero y se ejecuta movimiento máquina
    game.show_board()
    time.sleep(2)
    TCP_code_2 = game.cpu_move()
    
    # Se codifica mensaje de máquina
    print("TCP sent: " + TCP_code_2)
    """ Descomentar si se quiere probar conexion TCP-IP """
    TCPclient.mysend(TCP_code_2)

    # Se muestra tablero
    game.show_board()
    
if game.isWinner(1): 
    print("Ganaste!!!\n")
elif game.isWinner(2): 
    print("Perdise!!!\n")
else:
    print("Empate!!!\n")


"""
game.player_move("b2")
game.show_board()
time.sleep(1)
game.cpu_move()
game.show_board()
game.player_move("b2")
"""
