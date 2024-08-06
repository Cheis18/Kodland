# Mi Juego

Este es un juego arcade desarrollado en Python utilizando la librería Pygame. El objetivo es eliminar a todos los enemigos en cada nivel, con enemigos que se vuelven más rápidos y cambian de color en niveles posteriores.

## Requisitos

- Python 3.x
- Pygame (se puede instalar con `pip install pygame`)

## Cómo Jugar

1. Ejecuta el archivo `main.py` para iniciar el juego.
2. Al iniciar, se te presentará un menú de selección de niveles. Elige un nivel presionando `1`, `2`, o `3`.
3. El juego comenzará automáticamente después de seleccionar el nivel.
4. Usa las teclas de flecha izquierda y derecha para mover al jugador.
5. Presiona la barra espaciadora para disparar.
6. El objetivo es eliminar a todos los enemigos en el nivel. Si el enemigo toca al jugador o llega al fondo de la pantalla, el juego terminará.
7. Completa todos los niveles para ganar el juego.

## Niveles

- **Nivel 1**: Enemigos de color rojo, velocidad lenta.
- **Nivel 2**: Enemigos de color azul, velocidad media.
- **Nivel 3**: Enemigos de color verde, velocidad alta.

## Controles

- **Flecha izquierda**: Mover al jugador a la izquierda.
- **Flecha derecha**: Mover al jugador a la derecha.
- **Espacio**: Disparar proyectiles.

## Funcionalidades

- Menú de selección de niveles.
- Varios niveles con diferentes velocidades y colores de enemigos.
- Pantalla de "Perdiste" si el jugador es tocado por un enemigo o si un enemigo toca el fondo de la pantalla.
- Pantalla de victoria cuando se completan todos los niveles.

## Cómo Ejecutar

1. Clona este repositorio o descarga el archivo `main.py`.
2. Asegúrate de tener Python y Pygame instalados.
3. Ejecuta el juego con el comando:

   ```bash
   python main.py
