from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
# class UserManager(BaseUserManager):
#     def create_user(self,username,password=None):
#         if not username:
#             raise ValueError('Users must have a email')
#         if not password:
#             raise ValueError('Users must have a password')

#         scrumyuser=self.model(
#             username=self.username,
#         )
#         scrumyuser.set_password(password)
#         scrumyuser.save(using=self._db)
#         return scrumyuser
class ScrumyUser(models.Model):
    STATUS_CHOICES=(
        ('Owner','Owner'),
        ('Admin', 'Admin'),
        ('QA', 'Quality Analyst'),
        ('Developer', 'Developer'),
    )
    
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255,null=True, unique=True)
    email=models.EmailField(max_length=255, unique=True)
    password=models.CharField(max_length=255,null=True)
    role=models.CharField(max_length=255, choices=STATUS_CHOICES,default='Developer')
    date_created=models.DateTimeField('date_created',auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    last_login=models.DateTimeField(auto_now=True)
    
    # objects=UserManager()

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS=[]
    def __str__(self):
        return self.name
    # def has_perm(self, perm, obj=None):
    #     return True
    # def has_module_perms(self,app_label):
    #     return True
    
   

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





    
