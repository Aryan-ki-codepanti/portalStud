from django.shortcuts import redirect, render
from .models import User , MarkSheet
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    
    context = {
        
    }
    return render(request , "base/home.html" , context)

@login_required(login_url="/login")
def logout_student(request):
    logout(request)
    return redirect("Home")
