# Generated by Django 5.0.3 on 2024-03-29 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='hours_logged',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
    ]
