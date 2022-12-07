class Player():
    '''
    Cada jugador dispone de 3 fichas. Cada una de estas fichas puede estar en cualquier posición del tablero o no haber
    sido colocada sobre el mismo todavía. El tablero es el siguiente:
         1  2  3
         __ __ __
    a   |__|__|__|
    b   |__|__|__|
    c   |__|__|__|
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
            '3':None
        } 

        self.__symbol = symbol

    def set_player_token(self, token, pos): 
        """
        Asigna un valor de posición a uno de los tokens

        params: 
            :arg token: (int) 1, 2 or 3
            :arg pos  : (str) board position
        """

        self.__tokens[str(token)] = pos

    def get_player_token(self,token): 
        """
        Devuelve el valor de posición de 1 token concreto

        params: 
            :arg token: (int) 1, 2 or 3
        """

        return self.__tokens[str(token)]

    def get_player_tokens(self):
        """
        Devuelve los valores de posición de los 3 tokens del Player
        """

        return self.__tokens.values()
    
    def get_player_symbol(self, token): 
        """
        Devuelve el símbolo indexado de una de las fichas

        params: 
            :arg token: (int) Token index
        """

        return self.__symbol + str(token)


# USE EXAMPLE 
"""
p = Player("x")

p.set_player_token(1, 'a1')

print(p.get_player_tokens())
"""