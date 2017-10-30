# django
from django import forms
import laby.models as django_models

class GameForm(forms.ModelForm):
    class Meta:
        model = django_models.Game
        fields = ('blue_player',
                  'green_player',
                  'red_player',
                  'yellow_player')

        widgets = {
            'blue_player': forms.widgets.Select(attrs={'class':'form-control',
            'id':'bluePlayer'}),
            'green_player': forms.widgets.Select(attrs={'class':'form-control',
            'id':'greenPlayer'}),
            'red_player': forms.widgets.Select(attrs={'class':'form-control',
            'id':'redPlayer'}),
            'yellow_player': forms.widgets.Select(attrs={'class':'form-control',
            'id':'yellowPlayer'}),
            }

class PlayerForm(forms.ModelForm):
    class Meta:
        model = django_models.Player
        fields = ('name',)

        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control',
            'id': 'name',
            'placeholder' : 'Enter a name'})
            }