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
    goal_time = models.IntegerField(help_text="Enter the amount of time you spent on this goal today: ", default=0)

    def __str__(self):
        return self.goal_name

class Progress(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name 