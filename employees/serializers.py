from rest_framework import serializers
from .models import AppUserProfile, AppUser, EmployeeList, Conge, AssignMission, ITAEmployeeModel,RecruitmentRequest, TestModel
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta



class AppUserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = AppUser
        fields = ['id', 'fname', 'lname', 'user_email', 'role', 'access_code', 'token', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = AppUser.objects.create_user(password=password, **validated_data)
        return user

    def get_token(self, obj):
        refresh = RefreshToken.for_user(obj)
        refresh.set_exp(lifetime=timedelta(hours=1))  # 1 heure
        return str(refresh.access_token)


class ITAEMployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITAEmployeeModel
        fields = '__all__'
 

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeList
        fields = '__all__'


class CongeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conge
        fields = '__all__'

class AssignMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignMission
        fields = '__all__'

class RecruitmentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentRequest
        fields = '__all__'


class AppUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUserProfile
        fields = '__all__'