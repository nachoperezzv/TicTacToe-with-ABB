from utils.player import Player

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

    def __init__(self,symbol_player_1 = 'x', symbol_player_2='o') -> None:
        '''
        Inicialización de la clase. Inicio de jugadores 1 y 2 y simbolos asignados.
        '''
        self.__player1 = Player(symbol_player_1)
        self.__player2 = Player(symbol_player_2)
        self.__pos = {
            'a1':False, 'a2':False, 'a3':False,
            'b1':False, 'b2':False, 'b3':False,
            'c1':False, 'c2':False, 'c3':False
        }   
        pass

    def check_position_exists(self,new_pos) -> bool:
        '''
        Comprueba que la posición que se pasa existe en el tablero. Las posición validas serás la permutación de
        las letras [A-C] y los números [1-3]

        params:
            :arg new_pos     : (str) any non-occupied/existing pos on table [a1,a2,a3,b1,b2,b3,c1,c2,c3]
        '''
        return True if self.__pos.get(new_pos,None) != None else False 

    def check_position_non_occupied(self,new_pos) -> bool:
        '''
        Comprueba que la ficha/token del jugador que se indica se puede mover a la nueva posición asignada.
        Es decir, comprueba que no este ocupada ya por otra ficha. 
        
        Esta función esta planteada para que se llame después de la función check_position_exists()

        params: 
            :arg new_pos     : (str) any non-occupied/existing pos on table [a1,a2,a3,b1,b2,b3,c1,c2,c3]
        '''
        return self.__pos[new_pos]  

    def update_position(self,player,token,new_pos):
        '''
        Actualiza la posición en la clase tablero y la del jugador que ha movido la ficha.

        Esta función esta planteada para que se llame después de las funciones check_position_exists() y check_position_non_occupied()

        params: 
            :arg player: (int) 1 or 2
            :arg token : (str) any token of the player [1,2,3]
        '''

        p = self.__player1      \
            if int(player) == 1 \
            else self.__player2
        
        self.__pos[p[token]] = False
        self.__pos[new_pos]  = True
        
        p[token] = new_pos

        