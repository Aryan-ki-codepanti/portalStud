from django.contrib import admin
from .models import User , MarkSheet

# Register your models here.
admin.site.register((
    User,
    MarkSheet
    ))