from django.shortcuts import render
from rest_framework import viewsets,permissions,generics
from .models import Employee, Conge
from .serializers import EmployeeSerializer, CongeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-created_at')
    serializer_class = EmployeeSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]


class CongeViewSet(viewsets.ModelViewSet):
    queryset = Conge.objects.all()
    serializer_class = CongeSerializer
    permission_classes = [permissions.AllowAny]