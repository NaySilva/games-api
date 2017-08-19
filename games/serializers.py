from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'release_date', 'game_category')

    def is_empty(self, field):
        if field is None or field == '':
            raise serializers.ValidationError("O campo não pode ser vazio.")
        return field

    def is_registered(self, name):
        if Game.objects.filter(name=name):
            raise serializers.ValidationError("Já existe jogo com esse nome.")

    def validate_name(self, name):
        self.is_registered(name)
        return self.is_empty(name)

    def validate_game_category(self, game_category):
        return self.is_empty(game_category)

    def validate_release_date(self, release_date):
        return self.is_empty(release_date)
