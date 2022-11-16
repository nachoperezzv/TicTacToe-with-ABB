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
        self.__tokens = {
            '1':None,
            '2':None,
            '3':None
        } 

        self.__symbol = symbol
        pass