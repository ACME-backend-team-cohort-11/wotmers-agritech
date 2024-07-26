from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import FarmerProfile, BusinessProfile, ExpertProfile

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        if user.user_type == 'farmer':
            FarmerProfile.objects.create(user=user)
        elif user.user_type == 'business':
            BusinessProfile.objects.create(user=user)
        elif user.user_type == 'expert':
            ExpertProfile.objects.create(user=user)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
