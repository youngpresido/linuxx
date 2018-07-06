from django.shortcuts import render,get_object_or_404,redirect, render_to_response
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
from django.template import loader
from django.contrib.auth.hashers import make_password,check_password
from .models import GoalStatus, ScrumyGoals,ScrumyUser
from .forms import AddUserForm, AddTasks
from .forms import UserRegistration
import hashlib
from .authentication import EmailAuthBackend
from django.views.generic import ListView
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
# Create your views here.


def angular(request):
    return render(request,'index.html',{})


class GoalsView(ListView):
    queryset=ScrumyGoals.objects.all()
    template_name='goals.html'
    #context_object_name="object_list"
def allus(x):
    st=ScrumyUser.objects.filter(scrumygoals__status__name=x)
    ps=[]
    for t in st:
        ps.append(t)
    return set(ps)
def index(request):
    alluser=ScrumyUser.objects.all()
    userscount=alluser.count()
    user = ScrumyUser.objects.get(username=request.user.username)
    print(user)
    #user=ScrumyUser.objects.get(username=request.user.username)
    owner=user.role=="Owner"
    admin=user.role=='Admin'
    qa=user.role=='QA'
    developer=user.role=='Developer'
    print(owner)

    daily=allus('DTS')
    goals=allus('WTS')
    verify=allus('Verify')
    done=allus('Done')
    # for st in ScrumyUser.objects.all():
    #     for p in st.scrumygoals_set.all ():
    #         print(p.status)
    # for gol in goals.scrumygoals_set.all():
    #     print(gol.title)
    # return 
   
    print(request.user)
    return render(request,'indexs.html',{'allusers':alluser,
    'goals':goals,
    'daily':daily,
    'verify':verify, 
    'done':done, 
    'user':user,
     'owner':owner,
    'admin':admin,
    'qa':qa,
    'developer':developer,
    'userscount':userscount

    })
def move_task(request,task_id=None):
    user = ScrumyUser.objects.get(username=request.user.username)
    goals=ScrumyGoals.objects.get(pk=task_id)
    st=""
    print(goals.task)
    print(user.role)
    if request.method=='POST':
        form=AddTasks(request.POST, instance=goals)  
        stats=form.data['status']
        status=GoalStatus.objects.get(pk=stats).name
       
        print(status)
        print(form.data['title'])
        print(form.data['user_id'])
        print(form.data['task'])
        # print(status in ["DTS","Verify"]) 
        # print(user.role=="Owner")
        if user.role=="Owner":
            

            if form.is_valid():
                form.save()
                return redirect('index')
    
        elif user.role=="Admin" and status in ["DTS","Verify"]:
           

            if form.is_valid():
                form.save()
                return redirect('index')
        elif user.role=="QA" and status in ["Verify","Done"]:
            

            if form.is_valid():
                form.save()
                return redirect('indexs')
        elif user.role=="Developer" and status in ["WTS","DTS"]:
            form=AddTasks(request.POST, instance=goals)

            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form=AddTasks(instance=goals)
            st="not allowed"
    else:
        form=AddTasks(instance=goals)

    return render(request,'move_task.html',{'instance':goals, 'forms':form, 'st':st})

def add_task(request):
    
    if request.method=='POST':
        form=AddTasks(request.POST)

        if form.is_valid():
            addtask=form.save(commit=False)

            addtasks=ScrumyGoals.objects.create(
                title=form.cleaned_data.get('title'),
                task=form.cleaned_data.get('task'),
                user_id=form.cleaned_data.get('user_id'),
                status=form.cleaned_data.get('status')
            )
            return redirect('indexs')
    else:
        form=AddTasks(request.POST)
    return render(request,'add_task.html',{'forms':form})
# def authenticate(self, username=None, password=None):
#     try:
#         user=User.objects.get(email=username)
#         if user.check_password(password):
#             return user
#         return None
#     except ScrumyUser.DoesNotExist:
#         return None

# def get_user(self,user_id):
#     try:
#         return User.objects.get(pk=user_id)
#     except User.DoesNotExist:
#         return None

def add_user(request):
    if request.method=='POST':
        form=AddUserForm(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            # passs=authenticate(form.cleaned_data['password'])
            users=ScrumyUser.objects.create(
                name=form.cleaned_data.get('name'),
                email=form.clean_email(),
                password=make_password(form.clean_password2()),
                username=form.cleaned_data.get('username'),
                role=form.cleaned_data.get('role')
            )
            # auth_login(request,users)
            # print(auth_login)
            return redirect('indexs')
    else:
        form=AddUserForm(request.POST)
    return render(request,'add_user.html',{'forms':form})
# def check_auth(request):
#     user_object=ScrumyUser.objects.get(username__iexact=username)
#     if check_password(password,user_object.password):
#         login(request,user_object)
def test(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username)
    print(password)
    users=EmailAuthBackend.authenticate(request,username=username, password=password)
    print(users)
    if users is not None:
        auth_login(request,users,backend='bamidelescrumy.authentication.EmailAuthBackend')
        #print(auth_login(request,users))
        return redirect('indexs')
    else:
        return render(request, 'loginsystem.html',{})
    
        
        
def loginsystem(request):
    return render(request,'loginsystem.html',{})
def singleuser(request,id):
    try:
       users=ScrumyUser.objects.get(pk=id)
    except ScrumyUser.DoesNotExist:
        raise Http404('No user with this id')
    print(users)
    if request.method=='POST':
        form=AddUserForm(request.POST,instance=users)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('indexs')
        else:
            form=AddUserForm(request.POST,instance=users)
    else:
        form=AddUserForm(instance=users)

       

    
    return render(request,'edit_user.html',{'instance':users, 'forms':form})

# def signup(request):
# 	if request.method=='POST':
# 		form=UserRegistration(request.POST)
# 		if form.is_valid():
# 			users=form.save()
#             auth_login(request,user)
# 			return redirect('index')
#     else:
# 		form=UserRegistration()

# 	return render(request,'signup.html',{'form':form})