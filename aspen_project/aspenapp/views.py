from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AdventureSerializer   
from .models import Adventure
# Create your views here.
class AdventureView(viewsets.ModelViewSet):
    serializer_class = AdventureSerializer      
    queryset = Adventure.objects.all()
