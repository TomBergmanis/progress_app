from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from .models import Homepage, Goal
from .forms import GoalForm

# Create your views here.

def index(response):
    return render(response, "main/base.html", {"name": "Test"})

def home(response):
    return render(response, "main/home.html", {"name": "Home page"})

@login_required
def progress(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, "main/progress.html", {'goals': goals})

@login_required
def add_goal(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect("progress")
    else:
        form = GoalForm()
        
    return render(request, "main/add_goal.html", {'form':form})

def goal_added(request):
    return render(request, 'main/goal_added.html')