from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, FarmerProfileView, BusinessProfileView, ExpertProfileView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/profile/', UserProfileView.as_view(), name='profile'),
    path('api/farmer/', FarmerProfileView.as_view(), name='farmer'),
    path('api/business/', BusinessProfileView.as_view(), name='business'),
    path('api/expert/', ExpertProfileView.as_view(), name='expert'),
]
