from django.shortcuts import render,redirect
from django.contrib import messages
from . forms import UserRegisterForm
from django.contrib.auth import login,authenticate
from . models import Profile

# Create your views here.

# view to register a new user
def SignUp(request):
    if request.user.is_authenticated :
        messages.warning(request,"User Already Exist !")
        return redirect("mainApp:index")
    
    # instantiate a new form
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        full_name = form.cleaned_data.get("full_name")
        email = form.cleaned_data.get("email")
        phone = form.cleaned_data.get("phone")
        password = form.cleaned_data.get("password1")

    # log in user directly after successful registration
        user = authenticate(email = email , password = password)
        login(request , user)

        

    # updating profile model from the form
        profile = Profile.objects.get(user = request.user)
        profile.full_name = full_name
        profile.phone = phone
        profile.save()

        messages.success(request,f"Hello {full_name}, Your account was created successfully !")
        return redirect("mainApp:index")
    
    # context to export form variable
    context = {
        "form":form
    }

    return render (request,"authApp/signup.html",context)
