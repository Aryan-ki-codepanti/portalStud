from django.shortcuts import redirect, render
from .models import User, MarkSheet
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):

    if request.user.is_authenticated:
        marksheets = MarkSheet.objects.filter(student=request.user)
        marksheet_summary = []

        for marksheet in marksheets:

            marks = {
                "maths": marksheet.maths,
                "computer_science": marksheet.computer_science,
                "english": marksheet.english,
                "chemistry": marksheet.chemistry,
                "physics": marksheet.physics
            }

            marks_keyPairs = list(marks.items())
            marks_keyPairs.sort(key=lambda mark : mark[1])

            highest = marks_keyPairs[-1][1]
            lowest = marks_keyPairs[0][1]

            bestSubs = list(
                map( 
                    lambda mark: mark[0] , 
                    filter( 
                        lambda mark: mark[1] == highest , marks_keyPairs
                        )
                    )
                )

            worstSubs = list(
                map( 
                    lambda mark: mark[0] , 
                    filter( 
                        lambda mark: mark[1] == lowest , marks_keyPairs
                        )
                    )
                )

            print(bestSubs)
            print(worstSubs)

            summary = {
                "marksheet": marksheet,
                "avg": (marksheet.maths + marksheet.computer_science + marksheet.english + marksheet.physics + marksheet.chemistry)/5 ,
                "highest": highest,
                "lowest": lowest,
                "bestSubs":bestSubs ,
                "worstSubs": worstSubs 
            }

            marksheet_summary.append(summary)

        print(marksheet_summary)
        context = {
            "marksheets": marksheets,
            "marksheet_summary": marksheet_summary 
        }
    else:
        context = {

        }

    return render(request, "base/home.html", context)


@login_required(login_url="/login")
def logout_student(request):
    logout(request)
    return redirect("Home")
