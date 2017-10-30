# django
from django.conf.urls import url

# app
from . import views

app_name = 'laby'

urlpatterns = [

    # Home
    url(r'^$', views.HomeTemplateView.as_view(), name='default'),
    url(r'^home$', views.HomeTemplateView.as_view(), name='home'),

    ## Game
    #  Create
    url(r'^game/create$', views.GameCreateView.as_view(), name='game-create' ),
    #  List
    url(r'^game/list$', views.GameListView.as_view(), name='game-list' ),
    #  Play
    url(r'^game/(?P<pk>[0-9]+)/play$', views.GamePlayView.as_view(), name='game-play' ),

    ## Player
    #  Create
    url(r'^player/create$', views.PlayerCreateView.as_view(), name='player-create' ),
    #  Delete
    url(r'^player/(?P<pk>[0-9]+)/delete$', views.PlayerDeleteView.as_view(), name='player-delete' ),
    #  List
    url(r'^player/list$', views.PlayerListView.as_view(), name='player-list' ),
]