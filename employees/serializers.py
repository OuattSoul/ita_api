from rest_framework import serializers
from .models import Employee, Conge, AssignMission,RecruitmentRequest



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
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


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
