from django.urls import path
from . import views

urlpatterns = [
    path("" , views.home , name="Home") ,
    path("logout/" , views.logout_student , name="Logout"),
    path("login/" , views.login_student , name="Login"),
    path("register/" , views.register_student , name="Register"),
    path("marksheet/<int:id>" , views.viewMarksheet , name="MarksheetView"),
    path("delete-marksheet/<int:id>/" , views.deleteMarksheet , name="DeleteMarksheet"),
    path("update-marksheet/<int:id>/" , views.updateMarksheet , name="UpdateMarksheet"),
    path("add-marksheet/" , views.addMarksheet , name="AddMarksheet")
]
