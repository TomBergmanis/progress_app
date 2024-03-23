from django import forms    
# from django.contrib.auth.forms import UserChangeForm
from .models import Goal

class GoalForm(forms.ModelForm):

    class Meta:
        model = Goal
        fields = ["goal_name", "goal_description", "goal_time"]

class EditUserGoalForm(forms.ModelForm):
    
    class Meta:
        model = Goal
        fields = ["goal_name", "goal_description", "goal_time"]
        widgets = {
            'goal_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter goal title"}),
            'goal_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter goal description"}),
            'goal_time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Time spent on the goal"}),
        }