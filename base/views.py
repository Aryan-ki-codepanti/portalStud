from django.shortcuts import redirect, render

from base.utils import getMarksheetSummary
from .models import User, MarkSheet
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


# CRUD marksheets
def home(request):

    if request.user.is_authenticated:
        marksheets = MarkSheet.objects.filter(student=request.user)
        marksheet_summary = []
        for marksheet in marksheets:
            summary = getMarksheetSummary(marksheet)
            marksheet_summary.append(summary)

        context = {
            "marksheets": marksheets,
            "marksheet_summary": marksheet_summary 
        }

    else:
        context = {

        }

    return render(request, "base/home.html", context)

# Delete Marksheet
def deleteMarksheet(request , id):

    if request.method == "GET":
        return redirect("Home")

    marksheet = MarkSheet.objects.get(id=id)
    
    if (request.user != marksheet.student):
        return redirect("Home")
    
    marksheet.delete()
    return redirect("Home")

@login_required(login_url="/login")
def logout_student(request):
    logout(request)
    return redirect("Home")
