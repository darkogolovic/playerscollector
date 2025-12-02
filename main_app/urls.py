from django.urls import path
from .views import (
    PlayerListCreate, PlayerDetail,
    AddCoachToPlayer, RemoveCoachFromPlayer,
    TeamListCreate, TeamDetail,
    CoachListCreate, CoachDetail,CreateUserView,LoginView,VerifyUserView
)

urlpatterns = [
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
    path('players/', PlayerListCreate.as_view()),
    path('players/<int:id>/', PlayerDetail.as_view()),
    path('players/<int:player_id>/add_coach/<int:coach_id>/', AddCoachToPlayer.as_view()),
    path('players/<int:player_id>/remove_coach/<int:coach_id>/', RemoveCoachFromPlayer.as_view()),
    path('teams/', TeamListCreate.as_view()),
    path('teams/<int:id>/', TeamDetail.as_view()),
    path('coaches/', CoachListCreate.as_view()),
    path('coaches/<int:id>/', CoachDetail.as_view()),
]
