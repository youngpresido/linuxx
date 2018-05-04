from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from django.template import loader
from .models import GoalStatus, ScrumyGoals,ScrumyUser
from .forms import AddUserForm, AddTasks
from .forms import UserRegistration
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    alluser=ScrumyUser.objects.all()
    goals=ScrumyUser.objects.filter(scrumygoals__status__name='WTS')
    # for goal in goals:
    #     for gol in goal.scrumygoals_set.all():
    #         print(gol.title)
    return render(request,'index.html',{'allusers':alluser,'goals':goals})
def move_task(request,task_id=None):
    goals=ScrumyGoals.objects.get(pk=task_id)
    print(goals.task)
    if request.method=='POST':
        form=AddTasks(request.POST, instance=goals)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=AddTasks(instance=goals)

    return render(request,'move_task.html',{'instance':goals, 'forms':form})

def add_task(request):
    if request.method=='POST':
        form=AddTasks(request.POST)

        if form.is_valid():
            addtask=form.save(commit=False)
            addtask.save()

            addtasks=ScrumyGoals.objects.create(
                title=form.cleaned_data.get('title'),
                task=form.cleaned_data.get('task'),
                user_id=form.cleaned_data.get('user_id'),
                status=form.cleaned_data.get('status')
            )
            return redirect('index')
    else:
        form=AddTasks(request.POST)
    return render(request,'add_task.html',{'forms':form})

def add_user(request):
    if request.method=='POST':
        form=AddUserForm(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            user.save()

            users=ScrumyUser.objects.create(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email')
                #role=form.cleaned_data.get('role')
            )
            return redirect('index')
    else:
        form=AddUserForm(request.POST)
    return render(request,'add_user.html',{'forms':form})

def singleuser(request,id):
    try:
       users=ScrumyUser.objects.get(pk=id)
    except ScrumyUser.DoesNotExist:
        raise Http404('No user with this id')
    return render(request,'user.html',{'users':users})

# def signup(request):
# 	if request.method=='POST':
# 		form=UserRegistration(request.POST)
# 		if form.is_valid():
# 			user=form.save()
# 			auth_login(request,user)
# 			return redirect('index')
# 	else:
# 		form=UserRegistration()

# 	return render(request,'signup.html',{'form':form})