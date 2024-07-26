from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import FarmerProfile, BusinessProfile, ExpertProfile

User = get_user_model()

class FarmerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerProfile
        fields = '__all__'

class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = '__all__'

class ExpertProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertProfile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    farmer_profile = FarmerProfileSerializer(required=False)
    business_profile = BusinessProfileSerializer(required=False)
    expert_profile = ExpertProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_type', 'farmer_profile', 'business_profile', 'expert_profile')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'user_type')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            user_type=validated_data['user_type']
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        try:
            user = User.objects.get(email=obj['email'])
            if user:
                return {
                    'username': user.username,
                    'email': user.email,
                    'user_type': user.user_type,
                }
        except User.DoesNotExist:
            return None

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request=self.context.get('request'), email=email, password=password)
        if user and user.is_active:
            refresh = RefreshToken.for_user(user)
            return {
                'email': user.email,
                'token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'user': self.get_user(data),
            }
        raise serializers.ValidationError("Invalid credentials")
