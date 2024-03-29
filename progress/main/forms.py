from django import forms    
# from django.contrib.auth.forms import UserChangeForm
from .models import Goal

class GoalForm(forms.ModelForm):

    class Meta:
        model = Goal
        fields = ["goal_name", "goal_description", "goal_deadline"]

class EditUserGoalForm(forms.ModelForm):
    hours_logged = forms.DecimalField(label='Hours Spent', max_digits=10, decimal_places=2, required=False)
    

    class Meta:
        model = Goal
        fields = ["goal_name", "goal_description", "goal_deadline"]
        widgets = {
            'goal_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter goal title"}),
            'goal_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter goal description"}),
            'goal_deadline': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': "deadline date"}),
        }