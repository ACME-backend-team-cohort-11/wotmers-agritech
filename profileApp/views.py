from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    FarmerRegisterSerializer, BusinessRegisterSerializer, ExpertRegisterSerializer,
    LoginSerializer, UserSerializer, FarmerProfileSerializer, BusinessProfileSerializer, ExpertProfileSerializer
)
from .models import FarmerProfile, BusinessProfile, ExpertProfile

class FarmerRegisterView(generics.CreateAPIView):
    serializer_class = FarmerRegisterSerializer

class BusinessRegisterView(generics.CreateAPIView):
    serializer_class = BusinessRegisterSerializer

class ExpertRegisterView(generics.CreateAPIView):
    serializer_class = ExpertRegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class FarmerProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = FarmerProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = FarmerProfile.objects.all()
    
    def get_object(self):
        return self.queryset.get(user=self.request.user)

class BusinessProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = BusinessProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = BusinessProfile.objects.all()
    
    def get_object(self):
        return self.queryset.get(user=self.request.user)

class ExpertProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ExpertProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = ExpertProfile.objects.all()
    
    def get_object(self):
        return self.queryset.get(user=self.request.user)