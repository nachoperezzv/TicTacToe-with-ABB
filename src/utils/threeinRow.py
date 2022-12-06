from tablero import Tablero
from player import Player


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

    def player_move(self, player)
