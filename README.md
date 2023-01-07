# Tic Tac Toe 

## Índice
1. [Índice](#índice)
2. [Instalación](#instalación-y-ejecución)
3. [Clonación del repositorio](#clonar-el-repositorio)
4. [Entorno Virtual](#crear-un-entorno-virtual-y-activarlo)
5. [Instalación de Dependencias](#instale-las-dependencias-necesarias)
6. [Ejecución](#ejecute-la-app)
7. [ABB en simulación](#si-va-a-utilizar-el-abb-en-simulación)
8. [ABB real](#si-va-a-utlizar-el-abb-real)
9. [Implementación](#implementación)

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


### Si va a utilizar el ABB en simulación 

Cargando la estación desde `Archivo->Compartir->Unpack and Work`. Debe ejecutar tan solo la tarea en RAPID o la simulación desde RobotStudio. 

Cabe destacar que el servidor para la comunicación se puede encontrar tanto en local como en otra dirección a especificar. Ha de coincidir la dirección y el puerto empleado, configurados en la interfaz y en el módulo de RAPID encargado de la comunicación. 

### Si va a utilizar el ABB real

Tras cargar la estación de la misma manera. Debe realizar el traspaso de la tarea a la controladora del robot, conectándose vía Ethernet o Wifi (dependiendo de las comunicaciones que esta tenga configuradas). 

Para acceder a la controladora real desde RobotStudio puede incluirla desde `Archivo->En línea->Conexión con un clic`. Seguidamente se ha de traspasar la tarea completa (con sus módulos correspondientes) a la nueva controladora añadida, a partir de la virtual. Una vez realizado, se puede ejecutar de la misma manera que en simulación si el robot se encuentra en Automático, de otro modo, se deberá ejecutar y controlar la tarea desde la Flexpendant. 

Es destacable que en este caso el servidor para la comunicación TCP ha de encontrarse en la dirección de la controladora del robot, por lo que se ha de modificar la dirección configurada en la aplicación que gestiona la interfaz. 

## Implementación  

Las siguientes clases permiten gestionar la lógica del juego: 

  - Player -> Jugador con 5 fichas. Con ella se gestiona la posición de cada una de las fichas en el tablero.
  
  - Tablero -> Crea inicialmente un tablero vacío con 2 jugadores. Tiene métodos de comprobación de posiciones existentes, ocupadas, actualización de posiciones, devolución de información de los jugadores, del propio tablero, etc.
  
  - ThreeinRow -> Implementa el propio juego del 3 en raya. Gestiona la lógica de movimientos en el tablero, la inteligencia de la CPU o si la partida ha terminado.
  
Se ha optado por definir un tablero con 2 jugadores, teniendo cada uno 5 fichas, de manera que cada vez que se coloque una no se pueda mover. Para que la inteligencia de la CPU sea aplicable con un 'minimax' y no se complique la elección de qué ficha mover y posibles casos de jugadas infinitas. 

La siguiente clase permite gestionar la comunicación Interfaz-Robot: 

  - TCP -> Trabaja con el protocolo de comunicación empleado, implementa la parte cliente. Se conecta al socket cuando se desea enviar un mensaje, se codifica este y se envía y recibe el mensaje de confimación del servidor, tambíen permite la recepción y decodificación de los datos.
  


  
