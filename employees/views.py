from django.shortcuts import render
from rest_framework import viewsets,permissions,generics
from .models import AppUser, AppUserProfile, ITAEmployeeModel, TestModel, EmployeeList, Conge, AssignMission, RecruitmentRequest
from .serializers import AppUserListSerializer, AppUserProfileSerializer, AppUserSerializer, CodeLoginSerializer, EmployeeSerializer, CongeSerializer, AssignMissionSerializer, ITAEMployeeSerializer, RecruitmentRequestSerializer, TestSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from rest_framework.response import Response





class CodeLoginUserView(generics.GenericAPIView):
    serializer_class = CodeLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)

class RegisterUserView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

class AppUserListView(generics.ListAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserListSerializer

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

