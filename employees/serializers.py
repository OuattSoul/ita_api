from rest_framework import serializers
from .models import EmployeeList, Conge, AssignMission,RecruitmentRequest



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


