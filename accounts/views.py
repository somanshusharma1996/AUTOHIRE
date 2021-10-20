from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from home.models import Resume
from .forms import candidateform,employerform

def candidate_signup_view(request):
    if request.method == 'POST':
        form = candidateform(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            
            group = Group.objects.get(name='Candidate')
            user.groups.add(group)

            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            phoneNumber=request.POST.get('phone_number')
            file_field=request.FILES['resume']
            upload = Resume(First_name=first_name,Last_name=last_name,phoneNumber=phoneNumber,resume=file_field)
            upload.user=user
            upload.save()


            login(request, user)
            return redirect('home:index')
    else:
        form = candidateform()
    return render(request, 'accounts/signup.html', { 'form': form })

def employer_signup_view(request):
    if request.method == 'POST':
        form = employerform(request.POST)
        if form.is_valid():
            user = form.save()
            
            group = Group.objects.get(name='Employer')
            user.groups.add(group)

            login(request, user)
            return redirect('home:index')
    else:
        form = employerform()
    return render(request, 'accounts/signup.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('home:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def logout_view(request):
    # if (request.method == 'POST'):
    logout(request)
    return redirect('/')