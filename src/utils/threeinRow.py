from tablero import Tablero
import random 
import time
import platform
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
        
        self.__win_possibilities = {"line": ["a", "b", "c", "1", "2", "3"],
                     "diagonal": {"d1": ["a1", "b2", "c3"], "d2":["a3", "b2", "c1"]}}

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
        return self.__board.update_position(player,pos,isMove=True)

    def cpu_random_move(self, player = 2): 
        """
        Se mueve una ficha aleatoria a una posición aletoria que esté libre
        
        params
            :arg player: (int) Default 2nd player, cpu
        """

        occupied = True
        while occupied: 
            pos, occupied = random.choice(list(self.__board.get_board().items()))

        self.player_move(pos, player)

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
        if self.__board.empty_board():
            self.cpu_random_move()
        else: 
            depth = len(self.__board.empty_cells())
            pos,_ = self.__minimax(depth, isCpu=True)
            
            print("Movimiento  CPU: " + str(pos) + "\n")
            self.player_move(pos, player)

    def show_board(self): 
        """
        Muestra el tablero
        """
        #clear_window()
        self.__board.print_board()

    def get_board(self):
        return self.__board.get_board()

# USE EXAMPLE

game = ThreeInRow()

while not game.game_over():

    moved = False
    while not moved:
        move = str(input('Use [a1,..,c3]: '))
        moved = game.player_move(move)

    game.show_board()
    time.sleep(1)
    game.cpu_move()
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
