from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Entry

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirmpassword = request.POST["confirmpassword"]
        if password == confirmpassword:
            emp=Entry(username=username,password=password,confirmpassword=confirmpassword)
            emp.save()  
    return render(request, "signup.html")
def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user=Entry.object.get(username=username,password=password)
            if user :
                login(request,user) 
                return redirect("main.html")
    return render(request, "signin.html")
def home(request):
    return render(request,"main.html")
