from django.urls import path
from . import views

urlpatterns = [
    path("" , views.home , name="Home") ,
    path("logout/" , views.logout_student , name="Logout"),
    path("delete-marksheet/<int:id>" , views.deleteMarksheet , name="deleteMarksheet")
]
