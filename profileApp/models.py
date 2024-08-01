'''profileApp models'''
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('farmer', 'Farmer'),
        ('business', 'Business'),
        ('expert', 'Expert'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class FarmerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='farmer_profile')
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    farm_size = models.CharField(max_length=50)
    crop_types = models.CharField(max_length=255)
    livestock_types = models.CharField(max_length=255)
    membership_in_cooperatives = models.CharField(max_length=255)
    passport = models.ImageField(upload_to='passports/', blank=True, null=True)


class BusinessProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='business_profile')
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    business_type = models.CharField(max_length=50)
    products_or_services = models.TextField()
    license_number = models.CharField(max_length=50)
    passport = models.ImageField(upload_to='passports/', blank=True, null=True)


class ExpertProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='expert_profile')
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    field_of_expertise = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()
    certifications = models.TextField()
    passport = models.ImageField(upload_to='passports/', blank=True, null=True)

