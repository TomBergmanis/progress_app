from django import forms    
from .models import Goal

class GoalForm(forms.ModelForm):

    class Meta:
        model = Goal
        fields = ["goal_name", "goal_desc", "goal_time"]
