from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Homepage(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name 
    
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_name = models.CharField(max_length=100)
    goal_description = models.TextField()
    goal_deadline = models.DateTimeField(help_text="Add a date (mm/dd/yyyy) and a time (00:00) here.", null=True)
    target_hours = models.IntegerField(default=0)
    
    def __str__(self):
        return self.goal_name

class GoalLog(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    hours_logged = models.DecimalField(max_digits=10, decimal_places=2)
    date_logged = models.DateField(auto_now_add=True)

class Progress(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name 
    
