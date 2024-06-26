from django.urls import path
from . import views 

urlpatterns=[
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("add_goal/", views.add_goal, name="add_goal"),
    path("goal_added/", views.goal_added, name="goal_added"),
    path("progress/", views.progress, name="progress"),
    path("edit_goals/<int:pk>/", views.UpdateUserGoals.as_view(), name="edit_user_goal"),
    path("edit_goal/<int:pk>/", views.delete_goal, name="delete_goal"),
]