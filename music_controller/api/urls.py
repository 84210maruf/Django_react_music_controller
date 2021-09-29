from django.urls import path

from .views import RoomView, main

urlpatterns = [
    path('', main),
    path('home', RoomView.as_view())
]
