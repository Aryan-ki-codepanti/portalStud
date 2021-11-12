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
    name = models.CharField(max_length=200 , default="Unnamed")
    english = models.DecimalField(default=0 , decimal_places=1 , max_digits=5)
    maths = models.DecimalField(default=0 , decimal_places=1 , max_digits=5)
    physics = models.DecimalField(default=0 , decimal_places=1 , max_digits=5)
    chemistry = models.DecimalField(default=0 , decimal_places=1 , max_digits=5)
    computer_science = models.DecimalField(default=0 , decimal_places=1 , max_digits=5)
    grade = models.CharField(max_length=1 , default='A')

    student = models.ForeignKey(User , on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.student.username}"

