from django.shortcuts import render
from rest_framework import viewsets,permissions,generics
from .models import EmployeeList, Conge, AssignMission, RecruitmentRequest
from .serializers import EmployeeSerializer, CongeSerializer, AssignMissionSerializer, RecruitmentRequestSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class EmployeeListViewSet(viewsets.ModelViewSet):
    queryset = EmployeeList.objects.all().order_by('-created_at')
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

class RecruitmentRequestViewSet(viewsets.ModelViewSet):
    queryset = RecruitmentRequest.objects.all()
    serializer_class = RecruitmentRequestSerializer
    permission_classes = [permissions.AllowAny]



