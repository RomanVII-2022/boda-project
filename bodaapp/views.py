from django.shortcuts import render
from bodaapp.serializers import PersonnelSerializer
from bodaapp.models import Personnel
from rest_framework import viewsets

class PersonnelViewSet(viewsets.ModelViewSet):
    serializer_class = PersonnelSerializer
    queryset = Personnel.objects.all()
