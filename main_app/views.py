from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import Player, Team,Coach
from .serializers import PlayerSerializer, TeamSerializer, CoachSerializer


class PlayerListCreate(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'id'

class AddCoachToPlayer(APIView):
    def post(self, request, player_id, coach_id):
        player = Player.objects.get(id=player_id)
        coach = Coach.objects.get(id=coach_id)
        player.coaches.add(coach)
        return Response({'message': f'Coach {coach.name} added to Player {player.name}'})



class RemoveCoachFromPlayer(APIView):
    def post(self, request, player_id, coach_id):
        player = Player.objects.get(id=player_id)
        coach = Coach.objects.get(id=coach_id)
        player.coaches.remove(coach)
        return Response({'message': f'Coach {coach.name} removed from Player {player.name}'})
    
class TeamListCreate(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'id'

class CoachListCreate(generics.ListCreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
class CoachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    lookup_field = 'id'

