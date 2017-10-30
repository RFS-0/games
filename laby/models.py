# Django
from django.db import models as models

# Third parties
from jsonfield import JSONField as JSONField

class Game(models.Model):

    blue_player = models.ForeignKey(
        to = 'Player', 
        related_name = 'games_of_blue_player', 
        verbose_name = 'Blue player', 
        on_delete = models.DO_NOTHING,
        null = True)
    
    green_player = models.ForeignKey(
        to = 'Player', 
        related_name = 'games_of_green_player', 
        verbose_name = 'Green player', 
        on_delete = models.DO_NOTHING,
        null = True)
    
    red_player = models.ForeignKey(
        to = 'Player', 
        related_name = 'games_of_red_player', 
        verbose_name = 'Red player', 
        on_delete = models.DO_NOTHING,
        null = True)
    
    yellow_player = models.ForeignKey(
        to = 'Player', 
        related_name = 'games_of_yellow_player', 
        verbose_name = 'Yellow player', 
        on_delete = models.DO_NOTHING,
        null = True)

    game_state = JSONField(
        verbose_name = 'Game state'
    )

    evt_created = models.DateTimeField(
        verbose_name = 'Date created', 
        auto_now_add = True)

    evt_changed = models.DateTimeField(
        verbose_name = 'Time of last change',
        auto_now = True)

    def __str__(self):
        return 'PK of Game: (' + str(self.pk) + ')'

    def get_absolute_url(self):
        return reverse('dpmfa:model-detail', args=[self.id])

class GameLog(models.Model):

    game = models.ForeignKey(
        to = 'Game', 
        related_name = 'game_logs', 
        verbose_name = 'Game of Log', 
        on_delete = models.DO_NOTHING,
        null = True)

    game_state = JSONField(
        verbose_name = 'Game state'
    )

    score_of_blue_player = models.BigIntegerField(
        verbose_name = 'Score of blue player',
        null = True
    )
    
    score_of_green_player = models.BigIntegerField(
        verbose_name = 'Score of green player',
        null = True
    )
    score_of_red_player = models.BigIntegerField(
        verbose_name = 'Score of red player',
        null = True
    )
    score_of_yellow_player = models.BigIntegerField(
        verbose_name = 'Score of yellow player',
        null = True
    )

class Player(models.Model):

    BLUE = 'B'
    GREEN = 'G'
    RED = 'R'
    YELLOW = 'Y'

    COLORS = (
        (BLUE, 'Blue'),
        (GREEN, 'Green'),
        (RED, 'Red'),
        (YELLOW, 'Yellow'),
    )

    name = models.CharField(
        verbose_name = 'Name',
        max_length = 250,
        null = False    
    )

    most_recent_game = models.ForeignKey(
        to = 'Game', 
        related_name = 'current_players', 
        verbose_name = 'Most recent game', 
        on_delete = models.DO_NOTHING,
        null = True)

    current_color = models.CharField(
        choices = COLORS,
        verbose_name = 'Current color',
        max_length = 250,
        null = True
    )

    current_score = models.BigIntegerField(
        verbose_name = 'Score',
        null = True
    )

    game_history = models.ManyToManyField(
        to = 'Game',
        related_name = 'players', 
        verbose_name = 'Game history')

    def __str__(self):
        return self.name