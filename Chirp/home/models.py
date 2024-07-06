from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django import forms
from django.conf import settings

# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, request):
        data = request.POST
        if not data['username']:
            raise ValueError("No Username given")
        user = self.model(username=data['username'], email=data['email'])
        user.set_password(data['password'])
        user.name = data.get('name', None)
        user.bio = data.get('bio', None)
        user.headline = data.get('headline', None)
        user.profile_pic = request.FILES.get('profile_pic', None)
        user.save()

        return user;

    def authenticate(self, username, password):
        try:
            if not username:
                raise ValueError("No Username")
            if not password:
                raise ValueError("No Password")
            
            user = None
            try:
                user = UserModel.objects.get(username=username)
            except Exception as e:
                raise ValueError("No User Found")
            if user is None:
                raise ValueError("No User Found")
            if not user.check_password(password):
                raise ValueError("Wrong Password")
            else:
                return user

        except Exception as e:
            print(e)
            raise Exception(e)
        
    def create_superuser(self, username, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        # return self.create_user(, **extra_fields)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()


class UserModel(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(blank=True, upload_to='uploads/profiles/')
    headline = models.TextField(blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"
    
    objects = CustomUserManager();

    def __str__(self):
        return f'{self.username}, {self.email}'
    
class ChirpModel(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, upload_to='uploads/images')

    def __str__(self):
        return self.content;


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password', 'name', 'headline', 'bio', 'profile_pic')
