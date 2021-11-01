from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=60 , null=True)
    email = models.EmailField(unique=True , null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True , default="user.png")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username' ]

class MarkSheet(models.Model):
    english = models.DecimalField(default=0)
    maths = models.DecimalField(default=0)
    physics = models.DecimalField(default=0)
    chemistry = models.DecimalField(default=0)
    computer_science = models.DecimalField(default=0)
    grade = models.CharField(max_length=1 , default='A')

    student = models.ForeignKey(User , on_delete=models.CASCADE)

