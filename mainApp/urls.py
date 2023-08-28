# this file manages all the Urls and roots for the mainAPp
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
]