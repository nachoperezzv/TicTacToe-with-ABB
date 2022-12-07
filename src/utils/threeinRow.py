from tablero import Tablero
from player import Player
import random 

"""
COMBINAR EN ESTA CLASE SOLO LA LÓGICA DEL 3 EN RAYA
"""

class threeInRow: 
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

    def isWinner(self, player):

        """
        Comprueba si el jugador es ganador. 
        Se revisa si los 3 tokens de este se encuentran en una de las dos diagonales. 
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
                for v in values:
                
                    if l not in v: 
                        winner = False
                        break
                    else: 
                        winner = True

                if winner == True:
                    break
                
        return winner
    
    def game_over(self):
        """
        Comprueba si la partida ha terminado porque se tiene un ganador. 

        Devuelve quién ha ganado, en caso de que siga en juego 'False'.
        """
        if self.isWinner(1): 
            return 1
        elif self.isWinner(2): 
            return 2
        else:
            return False

    def __one_to_win(self,player) -> bool:
        """
        Comprueba si al jugador le falta 1 ficha para ser ganador. 
        
        Se revisa si 2 de los 3 tokens de este se encuentran en una de las dos diagonales. 
        También si se encuentran en la misma fila o columna.
        
        Método utilizado para aplicar inteligencia a la CPU

        params: 
            :arg player: (int) 1 or 2
        """

        """
        one = False

        values = self.__board.get_player_values(player)        

        # Comprobación de diagonales para los tokens del jugador
        if  ("a1" in values and "b2" in values) or \
            ("a1" in values and "c3" in values) or \
            ("b2" in values and "c3" in values) or \
            ("a3" in values and "b2" in values) or \
            ("a3" in values and "c1" in values) or \
            ("b2" in values and "c1" in values):
            one = True

        # Comprobación de si hay al menos 2 fichas en alguna de las
        # filas o columnas
        if not one:
            for l in self.__win_possibilities["line"]:
                for v in values:
                
                    if l not in v: 

                        free = 1
                        if free > 1: 
                            one = False
                            break                        
                    else: 
                        one = True

        return one
        """
        pass

    def player_move(self, player, token, pos) -> bool: 
        """
        Mueve la ficha de un jugador a una posición concreta. 

        Internamente el método 'update_position' del tablero comprueba si se puede 
        realizar el movimiento y si es así, actualiza la posición del token. 

        """
        return self.__board.update_position(player,token,pos)

    def cpu_random_move(self, player = 2): 
        """
        Se mueve una ficha aleatoria a una posición aletoria que esté libre
        
        params
            :arg player: (int) Default 2nd player, cpu
        """

        token = random.randrange(1,3)

        occupied = True
        while occupied: 
            pos, occupied = random.choice(list(self.__board.get_board().items()))

        self.__board.update_position(player,token,pos)

    def cpu_move(self, player = 2):
        """
        Se mueve una ficha de la cpu con 'inteligencia' a una posición si la partida 
        no ha terminado.  


        """

        if self.game_over():
            return False

        if self.__board.empty_board():
            self.cpu_random_move()
        else: 
            move = self.minimax()
            x,y = move
            
            if x == 1: 
                pos = "a" + str(y)
            elif x == 1: 
                pos = "b" + str(y)
            elif x == 1: 
                pos = "c" + str(y)
            
            self.__board.update_position(player,1,pos)        

        pass

    def minimax(self): 
        """
        Heurística para llegar al movimiento óptimo
        """
        pass
