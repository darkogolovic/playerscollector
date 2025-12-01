from django.urls import path
from .views import (
    PlayerListCreate, PlayerDetail,
    AddCoachToPlayer, RemoveCoachFromPlayer,
    TeamListCreate, TeamDetail,
    CoachListCreate, CoachDetail
)

urlpatterns = [

    path('players/', PlayerListCreate.as_view()),
    path('players/<int:id>/', PlayerDetail.as_view()),
    path('players/<int:player_id>/add_coach/<int:coach_id>/', AddCoachToPlayer.as_view()),
    path('players/<int:player_id>/remove_coach/<int:coach_id>/', RemoveCoachFromPlayer.as_view()),
    path('teams/', TeamListCreate.as_view()),
    path('teams/<int:id>/', TeamDetail.as_view()),
    path('coaches/', CoachListCreate.as_view()),
    path('coaches/<int:id>/', CoachDetail.as_view()),
]
