from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, serializers

from .models import Room
from .serializers import RoomSerializer

# Create your views here.


class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

def main(request):
    return HttpResponse('<h1>Hellow</h1>')
