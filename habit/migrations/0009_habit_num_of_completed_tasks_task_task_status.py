# Generated by Django 4.1 on 2024-03-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0008_alter_habit_goal_alter_habit_notes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='num_of_completed_tasks',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='task',
            name='task_status',
            field=models.CharField(default='In progress', max_length=255),
        ),
    ]
