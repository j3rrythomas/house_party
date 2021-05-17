
from django.urls import path

from .views import GetRoomView, JoinRoomView, RoomView, CreateRoomView, UserInRoom, LeaveRoomView, UpdateView


urlpatterns = [
    path('room', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoomView.as_view()),
    path('join-room', JoinRoomView.as_view()),
    path('user-in-room', UserInRoom.as_view()),
    path('leave-room', LeaveRoomView.as_view()),
    path('update-room', UpdateView.as_view())
]
