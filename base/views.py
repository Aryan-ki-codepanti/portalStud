from django.shortcuts import render
from .models import User , MarkSheet

# Create your views here.

def home(request):
    
    context = {
        
    }
    return render(request , "base/home.html" , context)

