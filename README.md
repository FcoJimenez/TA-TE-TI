
# Proyecto TA-TE-TI

1. Crear el Proyecto en Django
Primero, crea un proyecto y una aplicación en Django.

# bash
```tsx
django-admin startproject tictactoe_project
cd tictactoe_project
python manage.py startapp game
```
2. Definir el Modelo (game/models.py)

Vamos a crear un modelo simple que almacene los movimientos de las partidas. Usaremos un campo de texto para almacenar los movimientos, y guardaremos el estado de la partida.

```tsx
moves: Es un campo de texto donde se almacenan los movimientos como una cadena separada por comas. Ejemplo: 'X,O,X,,,' (las posiciones vacías se mantienen con ,).

check_winner(): Método que verifica si hay un ganador basado en los movimientos almacenados.
```
3. Formularios (game/forms.py)

Vamos a crear un formulario sencillo para registrar los movimientos de los jugadores.

4. Vistas (game/views.py)

Las vistas se simplifican para permitir la creación de una partida, registrar un movimiento, y verificar si hay un ganador.

```tsx
create_game: Crea una nueva partida y redirige a la vista de la partida.
play_game: Muestra el estado del juego y maneja la lógica para registrar movimientos. También comprueba si hay un ganador.
```
5. Plantillas (game/templates/game/play_game.html)

Ahora, la plantilla para mostrar el juego y los movimientos es sencilla:

6. Registro de URLs (game/urls.py)

Las URLs serán muy simples. Asegúrate de incluirlas en el archivo principal tictactoe_project/urls.py.

7. Registro en el Panel de Administración (game/admin.py)

Para poder ver las partidas en el panel de administración de Django, registra el modelo Game.

8. Migraciones y Arranque del Servidor

Ejecuta las migraciones y luego arranca el servidor.
# bash
```tsx
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```