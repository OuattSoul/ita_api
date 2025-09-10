from django.shortcuts import render
from rest_framework import viewsets,permissions,generics
from .models import AppUser, AppUserProfile, ITAEmployeeModel, TestModel, EmployeeList, Conge, AssignMission, RecruitmentRequest
from .serializers import AppUserProfileSerializer, AppUserSerializer, EmployeeSerializer, CongeSerializer, AssignMissionSerializer, ITAEMployeeSerializer, RecruitmentRequestSerializer, TestSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class RegisterUserView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer


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

class AppUserProfileViewSet(viewsets.ModelViewSet):
    queryset = AppUserProfile.objects.all()
    serializer_class = AppUserProfileSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer

class ITAEmployeeView(viewsets.ModelViewSet):
    queryset = ITAEmployeeModel.objects.all()
    serializer_class = ITAEMployeeSerializer

