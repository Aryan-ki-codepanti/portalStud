from django.shortcuts import redirect, render
from django.contrib import messages
from base.utils import getMarksheetSummary
from base.models import User, MarkSheet
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from base.forms import MarkSheetForm

# Create your views here.



# USER 
def login_student(request):
    
    if request.user.is_authenticated:
        return redirect("Home")

    if request.method == "POST":
        pass
    return render(request , "base/login.html")

def register_student(request):
    if request.user.is_authenticated:
        return redirect("Home")

    if request.method == "POST":
        pass
    return render(request , "base/register.html")

@login_required(login_url="/login")
def logout_student(request):
    messages.success(request , "Logged out successfully")
    logout(request)
    return redirect("Home")


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
@login_required(login_url="/login")
def deleteMarksheet(request , id):

    marksheet = MarkSheet.objects.get(id=id)
    if (request.user != marksheet.student):
        messages.error(request , "You are unauthorized to do so!")
        return redirect("Home")

    if request.method == "GET":
        context = {
            "marksheet" : marksheet
        }
        return render( request , "base/deleteMarksheet.html" , context )
    # POST Request handle Delete
    messages.success(request , "Marksheet deleted successfully") 
    marksheet.delete()
    return redirect("Home")

# Update Marksheet
@login_required(login_url="/login")
def updateMarksheet(request , id):
    marksheet = MarkSheet.objects.get(id=id)

    if (request.user != marksheet.student):
        messages.error(request , "You are unauthorized to do so!")
        return redirect("Home")

    if request.method == "GET":
        form = MarkSheetForm(instance=marksheet)
        
        context = {
            "marksheet" : marksheet,
            "form": form
        }
        return render( request , "base/updateMarksheet.html" , context )
        
    # POST : Update logic
    form = MarkSheetForm(data=request.POST , instance=marksheet)
    if form.is_valid():
        form.save()
    messages.success(request , "Marksheet updated  successfully") 
    return redirect("Home")

# Add Marksheet
@login_required(login_url="/login")
def addMarksheet(request):

    # POST request add logic
    if request.method == "POST":
        form = MarkSheetForm(data=request.POST)
        if form.is_valid():
            marksheet = form.save(commit=False)
            marksheet.student = request.user 
            marksheet.save()
            messages.success(request , "Marksheet added successfully")
            return redirect("Home")        

    form = MarkSheetForm()        
    context = {
        "form": form
    }
    return render( request , "base/addMarksheet.html" , context )
    

