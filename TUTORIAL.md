# GUÍA DE USUARIO

A continuación se explican los diferentes comandos y pantallas con las que el usuario podrá interactuar. Como usuario, no tiene que preocuparse por nada, por lo que si quiere acceder a la aplicación tan solo debe acceder a la pantalla principal pinchando [aquí](http://localhost:5000).

## Índice
1. [Índice](#índice)
2. [Conexión a Internet](#conexión-a-internet)
3. [Modos de Juego](#modos-de-juego)
4. [Cómo Jugar](#cómo-jugar)
5. [Configuración](#configuración)
6. [Tutorial](#tutorial)
7. [Otros](#otros)

## Conexión a Internet
Esta aplicación, de momento, se ejecuta de forma local, por lo que no requiere de conexión a internet para interactuar con el robot. Sin embargo, si quiere utilizar el reconocimiento por voz, si que deberá encontrarse conectado. 

## Modos de juego

![Modos de juego](/assets/png/modos_de_juego.png)

Se puede seleccionar entre dos tipos de juego diferentes: 

1. Modo UN JUGADOR
2. Modo DOS JUGADORES

Tras hacer la selección del modo de juego deberá introducir el nombre de los jugadores. Si ha elegido el modo UN JUGADOR deberá darle un nombre a la máquina y seleccionar uno para si mismo. Si ha elegido el modo DOS JUGADORES cada uno de los participantes deberá darse un nombre de jugador a si mismo. 

### Modo UN JUGADOR

Jugará contra la máquina. En este caso, usted, el jugador uno siempre tendrá el primer turno. En cuanto seleccione la siguiente casilla en la que colocar la pieza, la computadora procesará el siguiente movimiento y automaticamente lo verá reflejado en el casillero. Así mismo, independientemente de si esta jugando en simulación o en robot real, recomendamos unos segundos de espera antes de ejecutar el siguiente movimiento. Normalmente hasta que el robot acabe de mover ambas piezas. 

### Modo MULTIJUGADOR

En este caso, jugará contra otro compañero. Al igual que antes, el jugador 1 es el que comenzará sacando siempre. Deberán turnarse para seleccionar casillas, y de nuevo, se recomienda a los usuarios que esperen hasta que el robot haya colocado la pieza. 

## Cómo jugar

![Tablero](/assets/png/tablero.png)

Una vez se ha seleccionado el modo de juega deberá ir indicando a medida que progresa el juego donde quiere colocar la siguiente ficha. Esta acción de dos formas diferentes: 

1. Haciendo click sobre la pantalla.
2. Usando el reconocimiento por voz integrado. 

Debe tener en cuenta que el juego dura hasta que: 

1. Todas las casillas queden completas.
2. Cualquiera de los 2 jugadores se declare ganador.

### Click sobre la pantalla

Para usar este método no necesita de internet, ni realizar ninguna serie de comandos especiales. Cuando se indique su turno (lo verá reflejado en la pantalla), seleccione la casilla en la que quiere añadir una ficha y listo. 

### Reconocimiento de voz

Para esta opción es preciso que disponga de internet y que esté conectado al mismo. El tablero esta dividido en casillas enumeradas por letras y números. Desde la casilla superior izquierda a la casilla inferior derecha, moviendonos por filas, tendríamos que cada casilla recibe el siguiente nombre: 

```
A1, A2, A2, B1, B2, B3, C1, C2, C3 
```

Para indicar la posición a la que quiere mover la siguiente ficha, solo tiene que abrir el microfono (pulsando el botón), decir la posición, y cerrar el microfono (pulsandolo de nuevo). Un ejemplo podría ser: 

1. "Mueve la ficha a la posición A1"
2. "Ficha a posición B1"
3. "C1" 

## Configuración

![Configuracion](/assets/png/configuracion.png)

Dispone de una pantalla de configuración que le pedirá 2 cosas. 

1. Idioma y dialecto. Esto es importante para el reconocimiento de voz. Seleccione el dialecto adecuado ya que la calidad aumentará o decrecerá significativamente si no lo hace. 

2. Selección de IP y Puerto. En función del ABB que este utilzando y de uso (simulación o real) usará una IP y un PUERTO diferentes. Porfavor seleccione entre las múltiples opciones para conectarse correctamente. 

## Tutorial

![Tutorial](/assets/png/tutorial.png)

En caso de que tuviese alguna duda más, dispone de un tutorial completo de usuario en el propio juego, en una página especial llamada _**tutorial**_. No dude en acceder a ella para más información. 

## Otros

![Contacto](/assets/png/contacto.png)

Puede contactar con nosotros, acceder al repositorio oficial, o ver más información sobre los robots ABB a través de los enlaces que se dejan en la web. Por favor, no dude en visitarlos o en contactar con nosotros. 

