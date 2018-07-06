from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,username,password=None):
        if not username:
            raise ValueError('Users must have a username')
        if not password:
            raise ValueError('Users must have a password')

        user=self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_staffuser(self,username,password):
        user=self.create_user(username,password=password,)
        user.staff=True
        user.save(using=self._db)
        return user
    # def create_user(self,username,password=None, **extra_fields):
    #     extra_fields.setdefault('is_superuser', False)
    #     return self._create_user(username,password,**extra_fields)
    def create_superuser(self,username,password,**extra_fields):
        user=self.create_user(username,password=password,)
        user.staff=True
        user.admin=True
        user.save(using=self._db)
        return user
        # extra_fields.setdefault('is_superuser',True)

        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError('Superuser must have is_superuser=True.')
        # return self._create_user(username,password,**extra_fields)
class ScrumyUser(AbstractBaseUser):
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
    active=models.BooleanField(default=True)
    staff=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)
    objects=UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS=[]
    def __str__(self):
        return self.name
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    class Meta:
        verbose_name_plural="Scrumy User"
    def get_absolute_url(self):
        return reverse('scrumyuser-detail',args=self.pk)
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_active(self):
        return self.active

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
    class Meta:
        verbose_name_plural="Goal Status"
    def get_absolute_url(self):
        return reverse('goalstatus-detail',args=self.pk)
class ScrumyGoals(models.Model):
    user=models.ForeignKey('ScrumyUser',on_delete=models.CASCADE,related_name='scrumygoals')
    status=models.ForeignKey('GoalStatus',on_delete=models.CASCADE,related_name='scrumygoal')
    title=models.CharField(max_length=255,null=True)
    task=models.TextField()
    date_created=models.DateTimeField('date_created', auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="Scrumy Goals"
    def get_absolute_url(self):
        return reverse('scrumygoals-detail',args=[str(self.pk)])





    
