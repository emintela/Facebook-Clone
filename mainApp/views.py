from django.shortcuts import render

# Create your views here.

# main view to launch the index page 
def index(request):
    return render(request,"mainApp/index.html")
