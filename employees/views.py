from django.shortcuts import render
from rest_framework import viewsets,permissions,generics
from .models import Employee, Conge, AssignMission
from .serializers import EmployeeSerializer, CongeSerializer, AssignMissionSerializer
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

class AssignMissionViewSet(viewsets.ModelViewSet):
    queryset = AssignMission.objects.all()
    serializer_class = AssignMissionSerializer
    permission_classes = [permissions.AllowAny]