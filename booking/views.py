from distutils.command.upload import upload
from multiprocessing import context
from unicodedata import category
from django.shortcuts import render, redirect
from .models import Report,Category,Upload,Photo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
# Create your views here.
def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'booking/login_register.html', {'page': page})

def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                return redirect('home')

    context = {'form': form, 'page': page}
    return render(request, 'booking/login_register.html', context)
@login_required(login_url='login')
def home(request):
    projects_count = Upload.objects.all().filter(user=request.user).count()
    project_pending = Upload.objects.all().filter(user=request.user).filter(status="pending").count()
    project_done = Upload.objects.all().filter(user=request.user).filter(status="done").count()
    projects = Upload.objects.all().filter(user=request.user)
    context = {
        'count':projects_count,
        'pending': project_pending,
        'done':project_done,
        'projects':projects
    }
    return render(request,'booking/home.html',context)
@login_required(login_url='login')
def uploadData(request):
    user = request.user
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        category = categories.get(pk=int(data['category']))
        print()
        upload = Upload.objects.create(project_name=data['name'],category=category,user=request.user)
        images = request.FILES.getlist('images')

        for image in images:
            photo = Photo.objects.create(
                user = user,
                image=image,
            )
        return redirect('home')
    context = {'categories':categories}
    return render(request,'booking/upload.html',context)

@login_required(login_url='login')
def reports(request):
    reports = Report.objects.all().filter(user = request.user)
    context = {'reports':reports}
    return render(request,'booking/report.html',context)
    
@login_required(login_url='login')
def projects(request):
    projects = Upload.objects.all().filter(user=request.user)
    context = {'projects':projects}
    return render(request,'booking/projects.html',context)