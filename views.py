from django.shortcuts import render, redirect
from .models import Game
from .forms import MoveForm

def create_game(request):
    game = Game.objects.create()
    return redirect('play_game', game_id=game.id)

def play_game(request, game_id):
    game = Game.objects.get(id=game_id)
    winner = game.check_winner()
    
    if winner:
        game.status = 'finished'
        game.winner = winner
        game.save()

    if request.method == 'POST':
        form = MoveForm(request.POST)
        if form.is_valid():
            position = form.cleaned_data['position']
            player = form.cleaned_data['player']
            
            # Solo permitimos un movimiento en posiciones vacías
            moves = game.moves.split(',')
            if position >= len(moves):
                moves.extend([''] * (position + 1 - len(moves)))  # Ampliamos la lista de movimientos
            if moves[position] == '':
                moves[position] = player
                game.moves = ','.join(moves)
                game.save()
                return redirect('play_game', game_id=game.id)
    else:
        form = MoveForm()

    return render(request, 'game/play_game.html', {'game': game, 'form': form, 'winner': winner})
