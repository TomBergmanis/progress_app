from typing import Any
from django.db.models.base import Model as Model
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required 
from .models import Homepage, Goal
from .forms import GoalForm, EditUserGoalForm
from django.urls import reverse


# Create your views here.

def index(response):
    return render(response, "main/base.html", {"name": "Test"})

def home(response):
    return render(response, "main/home.html", {"name": "Home page"})

# User can add new goals to their profile
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

# Success message when the user creates a new goal 
def goal_added(request):
    return render(request, 'main/goal_added.html')

# User can delete specific goals 
def delete_goal(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    print(get_object_or_404(Goal, pk=pk))
    print("goal selected for deletion is: ", goal.pk)

    if request.method == 'POST':
        print("goal: ", goal.pk, "has been deleted")
        goal.delete()
        return redirect('progress')
    
    return render(request, 'main/progress.html', {'goal':goal})

# User can edit and update their goals and then view them in the progress view
class UpdateUserGoals(generic.UpdateView):
    form_class = EditUserGoalForm
    template_name = "main/edit_user_goal.html"
    success_url = "/progress/"


    def get_object(self):
        return get_object_or_404(Goal, pk=self.kwargs['pk'], user=self.request.user)

    def form_valid(self, form):
        goal = form.save(commit=False)
        goal.user = self.request.user
        goal.save()
        return super().form_valid(form)

 # User can see their goals as a list 
@login_required
def progress(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, "main/progress.html", {'goals': goals})
