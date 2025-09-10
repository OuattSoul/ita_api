from rest_framework import serializers
from .models import AppUserProfile, AppUser, EmployeeList, Conge, AssignMission, ITAEmployeeModel,RecruitmentRequest, TestModel
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta
from .utils import send_welcome_email


class AppUserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = AppUser
        fields = ['id', 'fname', 'lname', 'user_email', 'role', 'access_code', 'token', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        """
        Vérifie que le mot de passe contient au moins 8 caractères
        """
        if len(value) < 8:
            raise serializers.ValidationError("Le mot de passe doit contenir au moins 8 caractères.")
        return value
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = AppUser.objects.create_user(password=password, **validated_data)

        # Envoi de l'email de bienvenue
        send_welcome_email(user_email=user.user_email, fname=user.fname, access_code=user.access_code)

        return user

    def get_token(self, obj):
        refresh = RefreshToken.for_user(obj)
        refresh.set_exp(lifetime=timedelta(hours=1))  # 1 heure
        return str(refresh.access_token)

class AppUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'fname', 'lname', 'user_email', 'role', 'access_code']


class CodeLoginSerializer(serializers.Serializer):
    #user_email = serializers.EmailField()
    access_code = serializers.CharField(max_length=4, write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        #email = data.get('user_email')
        code = data.get('access_code')

        try:
            user = AppUser.objects.get(access_code=code)
        except AppUser.DoesNotExist:
            raise serializers.ValidationError("Utilisateur non trouvé")

        if user.access_code != code:
            raise serializers.ValidationError("Code d'accès incorrect")

        # Générer un token JWT d'une heure
        refresh = RefreshToken.for_user(user)
        refresh.set_exp(lifetime=3600)  # 1 heure
        data['token'] = str(refresh.access_token)
        data['user_id'] = user.id
        data['fname'] = user.fname
        data['lname'] = user.lname
        data['role'] = user.role
        return data
    
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