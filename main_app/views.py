from rest_framework.response import Response
from rest_framework import generics,status, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Player, Team,Coach
from .serializers import PlayerSerializer, TeamSerializer, CoachSerializer,UserSerializer
from rest_framework.exceptions import PermissionDenied

class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': response.data
    })

# User Login
class LoginView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
      })
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class VerifyUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        refresh = RefreshToken.for_user(request.user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": UserSerializer(request.user).data
        })



class PlayerListCreate(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
     
      user = self.request.user
      return Player.objects.filter(user=user)

    def perform_create(self, serializer):
      serializer.save(user=self.request.user)

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Player.objects.filter(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        player = self.get_object()
        serializer = self.get_serializer(player)

        
        coaches_not_associated = Coach.objects.exclude(id__in=player.coaches.all())
        coaches_serializer = CoachSerializer(coaches_not_associated, many=True)

        return Response({
            "player": serializer.data,
            "coaches_not_associated": coaches_serializer.data
        })

    def perform_update(self, serializer):
        player = self.get_object()
        if player.user != self.request.user:
            raise PermissionDenied("You do not own this player.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("You do not own this player.")
        instance.delete()


class AddCoachToPlayer(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, player_id, coach_id):
        player = Player.objects.get(id=player_id)

        if player.user != request.user:
            raise PermissionDenied("You do not own this player.")

        coach = Coach.objects.get(id=coach_id)
        player.coaches.add(coach)

        return Response({"message": f"Coach {coach.name} added to Player {player.name}"})


class RemoveCoachFromPlayer(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, player_id, coach_id):
        player = Player.objects.get(id=player_id)

        if player.user != request.user:
            raise PermissionDenied("You do not own this player.")

        coach = Coach.objects.get(id=coach_id)
        player.coaches.remove(coach)

        return Response({"message": f"Coach {coach.name} removed from Player {player.name}"})

    
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

