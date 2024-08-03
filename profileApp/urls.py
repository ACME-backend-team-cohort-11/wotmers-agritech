from django.urls import path
from .views import (
    FarmerRegisterView, BusinessRegisterView, ExpertRegisterView,
    LoginView, UserProfileView, FarmerProfileView, BusinessProfileView, ExpertProfileView
)

urlpatterns = [
    path('register/farmer/', FarmerRegisterView.as_view(), name='register-farmer'),
    path('register/business/', BusinessRegisterView.as_view(), name='register-business'),
    path('register/expert/', ExpertRegisterView.as_view(), name='register-expert'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/farmer/', FarmerProfileView.as_view(), name='farmer-profile'),
    path('profile/business/', BusinessProfileView.as_view(), name='business-profile'),
    path('profile/expert/', ExpertProfileView.as_view(), name='expert-profile'),
]