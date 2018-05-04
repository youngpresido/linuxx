from django.db import models
from django.utils import timezone

# Create your models here.

class ScrumyUser(models.Model):
    STATUS_CHOICES=(
        ('Owner','Owner'),
        ('Admin', 'Admin'),
        ('QA', 'Quality Analyst'),
        ('Developer', 'Developer'),
    )
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    role=models.CharField(max_length=255, choices=STATUS_CHOICES,default='Developer')
    date_created=models.DateTimeField('date_created',auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name


class GoalStatus(models.Model):
    GOAL_TYPE = (
        ('Done', 'Done'),
        ('Verify', 'Verified'),
        ('WTS', 'WeeklyStatus'),
        ('DTS', 'DailyStatus'),

    )
    name=models.CharField(max_length=255,choices=GOAL_TYPE,default='DTS')

    def __str__(self):
        return self.name
class ScrumyGoals(models.Model):
    user_id=models.ForeignKey(ScrumyUser,on_delete=models.CASCADE)
    status=models.ForeignKey(GoalStatus,on_delete=models.CASCADE)
    title=models.CharField(max_length=255,null=True)
    task=models.TextField()
    date_created=models.DateTimeField('date_created', auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title





    
