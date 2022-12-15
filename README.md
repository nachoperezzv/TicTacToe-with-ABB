# Juego 3 en Raya 

Implementadas clases: 

  - Player -> Jugador con 5 fichas. Con ella se gestiona la posición de cada una de las fichas en el tablero.
  
  - Tablero -> Crea inicialmente un tablero vacío con 2 jugadores. Tiene métodos de comprobación de posiciones existentes, ocupadas, actualización de posiciones, devolución de información de los jugadores, del propio tablero...
  
  - ThreeinRow -> Implementa el propio juego del 3 en raya. Gestiona la lógica de movimientos en el tablero, la inteligencia de la CPU, si la partida ha terminado...
  
Se ha optado por definir un tablero con 2 jugadores, teniendo cada uno 5 fichas, de manera que cada vez que se coloque una no se pueda mover. Para que la inteligencia de la CPU sea aplicable con un 'minimax' y no se complique la elección de qué ficha mover y posibles casos de jugadas infinitas. 

## Por implementar ##

  - Mensajes TCP a partir de casillas por reconocimiento de voz
  
