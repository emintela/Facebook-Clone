# urls for the auth app
from django.urls import path
from . views import SignUp

app_name = "authApp"

urlpatterns = [
    path("signup/",SignUp, name="signup"),

]