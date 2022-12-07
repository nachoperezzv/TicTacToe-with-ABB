from player import Player

class Tablero():
    '''
    Tablero virtual para comprobar las posiciones. 
    Cada jugador dispone de 3 fichas numeradas. 
         1  2  3
         __ __ __
    a   |__|__|__|
    b   |__|__|__|
    c   |__|__|__|    
    :arg symbol_player_1: Indica el símbolo asignado del jugador 1
    :arg symbol_player_2: Indica el símbolo asignado del jugador 2
    '''

    def __init__(self,symbol_player_1 = 'x', symbol_player_2 = 'o') -> None:
        '''
        Inicialización de la clase. Inicio de jugadores 1 y 2 y simbolos asignados.
        Instanciación del tablero con todas las casillas libres. 
        
        params:
            :arg symbol_player_1: (str) for player1
            :arg symbol_player_1: (str) for player2
        '''
        self.__player1 = Player(symbol_player_1)
        self.__player2 = Player(symbol_player_2)
        self.__pos = {
            'a1':None, 'a2':None, 'a3':None,
            'b1':None, 'b2':None, 'b3':None,
            'c1':None, 'c2':None, 'c3':None
        }   

    def __check_position_exists(self,new_pos) -> bool:
        '''
        Comprueba que la posición que se pasa existe en el tablero. Las posición validas serás la permutación de
        las letras [A-C] y los números [1-3]
        
        params:
            :arg new_pos     : (str) any non-occupied/existing pos on table [a1,a2,a3,b1,b2,b3,c1,c2,c3]
        '''

        return True if self.__pos.get(new_pos,False) != False else False

    def __check_position_non_occupied(self,new_pos) -> bool:
        '''
        Comprueba que la ficha/token del jugador que se indica se puede mover a la nueva posición asignada.
        Es decir, comprueba que no este ocupada ya por otra ficha. 
        
        Esta función esta planteada para que se llame después de la función check_position_exists()
        
        params: 
            :arg new_pos     : (str) any non-occupied/existing pos on table [a1,a2,a3,b1,b2,b3,c1,c2,c3]
        '''

        return self.__pos[new_pos]  

    def update_position(self,player,token,new_pos) -> bool:
        '''
        Actualiza la posición en la clase tablero y la del jugador que ha movido la ficha.
        
        ###Esta función esta planteada para que se llame después de las funciones check_position_exists() y check_position_non_occupied()
        
        Para actualizar una posición antes se comprueba si existe y está ocupada

        params: 
            :arg player : (int) 1 or 2
            :arg token  : (str) any token of the player [1,2,3]
            :arg new_pos: (str) any position of the board [a1...c3]
        '''
        if self.__check_position_exists(new_pos):
            if not self.__check_position_non_occupied(new_pos):
                p = self.__player1      \
                    if int(player) == 1 \
                    else self.__player2

                # Si la ficha está en el tablero su antigua posición se pone a False
                if p.get_player_token(token) != None:
                    self.__pos[p.get_player_token(token)] = None  

                self.__pos[new_pos]  = p.get_player_symbol(token)
                
                p.set_player_token(token, new_pos)
                
                possible = True
        
        else: 
            # ESTO DEBERÍA COMUNICARSE AL FRONT Y MOSTRARLO POR AHÍ, DE MOMENTO LO MUESTRO POR 
            # PANTALLA, PODRÍA RETORNARSE 'TRUE' SI SE HA PODIDO MOVER PARA GESTIONAR EL MENSAJE
            # DESDE FUERA
            print("No es posible mover la ficha a esa posición, inténtelo de nuevo")
            possible = False

        return possible
    
    def get_player_values(self,player):
        """
        Retorna el objeto del jugador solicitado. 

        params: 
            :arg player: (int) 1 or 2
        """
        
        p = self.__player1      \
            if int(player) == 1 \
            else self.__player2

        return p.get_player_tokens()   

    def get_board(self): 

        """ 
        Devuelve una copia del tablero para leer sus valores
        """
        return self.__pos

    def empty_board(self): 
        """
        Comprueba si el tablero está vacío
        """

        empty = True
        #print(self.__pos.values())
        for v in self.__pos.values():

            if v != None:
                empty = False

        return empty


# USE EXAMPLE
"""
t = Tablero()

print(t.empty_board())
print(t.get_board())

n_player = 1
n_token = 2
pos = "a3"
t.update_position(player=n_player, token=n_token, new_pos=pos)

print(t.empty_board())
print(t.get_board())

print(t.get_player_values(n_player))
"""