from django import forms

class MoveForm(forms.Form):
    position = forms.IntegerField(min_value=0, max_value=8, label="Posición (0-8)")
    player = forms.ChoiceField(choices=[('X', 'Jugador X'), ('O', 'Jugador O')], label="Jugador")
