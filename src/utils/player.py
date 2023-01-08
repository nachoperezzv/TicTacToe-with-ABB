class Player():
    '''
    Cada jugador dispone de 3 fichas. Cada una de estas fichas puede estar en cualquier posición del tablero o no haber
    sido colocada sobre el mismo todavía. El tablero es el siguiente:
         1  2  3
         __ __ __
    A   |__|__|__|
    B   |__|__|__|
    C   |__|__|__|
    params:
        :arg symbol: Se escoge un caracter utf-8 para representar a cada jugador. Los carácteres típicos suelen ser X / O
    '''

    def __init__(self,symbol) -> None:
        """
        Instancia un objeto 'jugador' del que crea 3 fichas sin posición inicialmente

        params: 
            :args symbol:  (str) usually x or o
        """

        self.__tokens = {
            '1':None,
            '2':None,
            '3':None, 
            '4':None, 
            '5':None
        } 

        self.__symbol = symbol

        self.__usedTokens = 0

    def set_player_token(self, pos): 
        """
        Asigna un valor de posición a uno de los tokens libres

        params: 
            :arg pos  : (str) board position
        """

        self.__tokens[str(self.__usedTokens + 1)] = pos
        self.__usedTokens += 1

    
    def get_player_token(self,token): 
        """
        Devuelve el valor de posición de 1 token concreto

        params: 
            :arg token: (int) 1, 2, 3...
        """
        return self.__tokens[str(token)]

    def get_current_free_token(self):
        """
        Devuelve la siguiente ficha disponible para mover
        """

        return self.__usedTokens

    def get_player_tokens(self):
        """
        Devuelve los valores de posición de los tokens del Player
        """

        return self.__tokens.values()
    
    def get_player_symbol(self): 
        """
        Devuelve el símbolo que representa al jugador
        """

        return self.__symbol

    def reset_tokens(self):
        """
        Elimina las asignaciones de posición de las fichas del jugador
        """
        self.__tokens = {
            '1':None,
            '2':None,
            '3':None, 
            '4':None, 
            '5':None
        } 

        self.__usedTokens = 0


# USE EXAMPLE 
"""
p = Player("x")

p.set_player_token('a1')

print(p.get_player_tokens())
"""