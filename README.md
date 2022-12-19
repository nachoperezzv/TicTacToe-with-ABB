# Tic Tac Toe 

## Índice
1. [Índice](#Índice)
2. [Instalación](#instalacion-y-ejecucion)


## Instalación y ejecución

Acceda al terminal `cmd` de windows o al `prompt` de Anaconda. Desde la carpeta donde quiera tener el repositorio ejecute los siguientes comandos en el terminal

### Clonar el repositorio

```
git clone https://github.com/nachoperezzv/servicios.git
```

### Crear un entorno virtual y activarlo
Al ejecutar el comando `dir` desde el `cmd` o `prompt`, debería poder ver la nueva carpeta con el repositorio. 

Desde la misma ubicación en la que ha clonado el repositorio y en la que se encuentra, ejecute lo siguiente. 

```
python -m venv servicios
```

Esto creará un entorno virtual. Una vez haya acabado de instalarse el entorno, acceda al repositorio y activelo.

```
cd servicios
.\Scripts\activate
```

Deberia de poder ver a la izquierda de su terminal como el entorno se ha activado. Si desea desactivarlo tan solo tiene que cerrar el terminal o, desde la misma ubicación que antes, realizar lo siguiente: 

```
.\Scripts\deactivate
```

### Instale las dependencias necesarias

Con el entorno ya activado, instale las dependencias que necesita para ejecutar la aplicación. 

```
pip install -r requirements.txt
```

Esto puede llevar unos minutos

### Ejecute la app

Para ejecutar la app dirijase a la carpeta `/src`. La primera ejecución descargará algunos modelos de reconocimiento de intenciones que se utilizan en la aplicación. Estos modelos quedan guardados en la caché, por lo que las siguientes ejecuciones son más rápidas. 

```
cd src/
python app.py
```


### Si va a usar los ABB en simulación ...

### Si va a usar los ABB reales ...

## Apuntes

Implementadas clases: 

  - Player -> Jugador con 5 fichas. Con ella se gestiona la posición de cada una de las fichas en el tablero.
  
  - Tablero -> Crea inicialmente un tablero vacío con 2 jugadores. Tiene métodos de comprobación de posiciones existentes, ocupadas, actualización de posiciones, devolución de información de los jugadores, del propio tablero...
  
  - ThreeinRow -> Implementa el propio juego del 3 en raya. Gestiona la lógica de movimientos en el tablero, la inteligencia de la CPU, si la partida ha terminado...
  
Se ha optado por definir un tablero con 2 jugadores, teniendo cada uno 5 fichas, de manera que cada vez que se coloque una no se pueda mover. Para que la inteligencia de la CPU sea aplicable con un 'minimax' y no se complique la elección de qué ficha mover y posibles casos de jugadas infinitas. 


  
