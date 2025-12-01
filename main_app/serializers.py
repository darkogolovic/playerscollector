from rest_framework import serializers
from .models import Player, Team,  Coach



class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    coaches = CoachSerializer(many=True, read_only=True)
    team = TeamSerializer(read_only=True)

    class Meta:
        model = Player
        fields = '__all__'
