# django
import django.views.generic as generic
import django.urls as urls

# app
import laby.models as models
import laby.forms as forms

class HomeTemplateView(generic.TemplateView):
    template_name = 'home.html'

class GameCreateView(generic.CreateView):
    model = models.Game
    form_class = forms.GameForm
    template_name = 'game_form.html'
    success_url = urls.reverse_lazy('laby:game-list')

class GameListView(generic.TemplateView):
    model = models.Game
    context_object_name = 'games'
    template_name = 'game_list.html'

class GamePlayView(generic.TemplateView):
    template_name = 'game_play.html'

class PlayerCreateView(generic.CreateView):
    model = models.Player
    form_class = forms.PlayerForm
    template_name = 'player_form.html'
    success_url = urls.reverse_lazy('laby:player-list')

class PlayerDeleteView(generic.DeleteView):
    model = models.Player
    form_class = forms.PlayerForm
    template_name = 'player_confirm_delete.html'
    success_url = urls.reverse_lazy('laby:player-list')

class PlayerListView(generic.ListView):
    model = models.Player
    context_object_name = 'players'
    template_name = 'player_list.html'