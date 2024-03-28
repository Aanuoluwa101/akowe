from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        print("calling create user in the custom user manager")
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields) #self.model returns an instance of the class to which
                                                      #this manager has been tied
        user.set_password(password)    #the set_password method is a method of the AbstractUser class
        user.save()
        return user
        
        
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff") or not extra_fields.get("is_superuser"):
            raise ValueError("is_staff and is_superuser must be True")
        
        self.create_user(email=email, password=password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username
    

