# Generated by Django 5.0.3 on 2024-03-29 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_progress_hours_logged_goal_hours_logged'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='hours_logged',
        ),
    ]
