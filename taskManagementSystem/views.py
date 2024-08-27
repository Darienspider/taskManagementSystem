from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView as AuthLoginView

def home (request):
    context = {
        "title":" Task Management System"
    }
    return render(request,"taskManagementSystem/home.html",context=context)

def test_login(request):
    username = 'testuser'
    password = 'testpassword'
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("User is authenticated")
    else:
        return HttpResponse("Authentication failed")
    
def loginView (AuthLoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('/tasks/') 
    