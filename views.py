from django.shortcuts import render
from rest_framework import viewsets
from .models import Moviedata
from .serializers import MovieSerializer




# Create your views here.


class MovieViewset(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer


class ActionViewset(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre="action")
    serializer_class = MovieSerializer

class ComedyViewset(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre="comedy")
    serializer_class = MovieSerializer



