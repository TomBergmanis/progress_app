# Generated by Django 5.0.3 on 2024-03-29 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal_deadline',
            field=models.DateTimeField(help_text='Add a date (mm/dd/yyyy) and a time (00:00) here.', null=True),
        ),
        migrations.CreateModel(
            name='GoalLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_logged', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_logged', models.DateField(auto_now_add=True)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.goal')),
            ],
        ),
    ]
