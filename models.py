from django.db import models

class Game(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'En progreso'),
        ('finished', 'Terminado'),
    ]
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    moves = models.TextField(default="")  # Guardamos los movimientos en un formato sencillo como cadena
    winner = models.CharField(max_length=1, blank=True, null=True)  # Puede ser 'X', 'O' o None
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Partida {self.id} - {self.status}"

    def check_winner(self):
        # Comprobamos si hay un ganador tras cada movimiento.
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columnas
            [0, 4, 8], [2, 4, 6],  # diagonales
        ]
        moves = self.moves.split(',')
        for pattern in win_patterns:
            x, y, z = pattern
            if len(moves) > z and moves[x] == moves[y] == moves[z] and moves[x] != '':
                return moves[x]
        return None
