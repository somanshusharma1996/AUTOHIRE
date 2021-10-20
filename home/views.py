from django.core.checks import messages
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from home.models import Resume,Job,recive_job_applications,afterapply
from .form import *
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
	job = Job.objects.all()
	return render(request, 'home/index.html', {'job':job})

# def resume(request):
# 	return render(request, 'home/resume.html', {})


class JobCreateView(LoginRequiredMixin,CreateView):
	model=Job
	fields=['user','title','description','location','type','category','last_date','company_name','company_description','website','created_at','filled']

	def form_valid (self,form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

def job_detail (request,pk):
	job = Job.objects.filter(pk=pk).first()
	return render(request, 'home/job_detail.html',{'job':job})



def open_resume(request, pk):
    recieve = recive_job_applications.objects.get(pk = pk)
    resume = getattr(recieve, 'resume')
    response = redirect(f'{resume}')
    return response

#for candidate

def job_create_list(request):
	jobcreate = Job.objects.all()
	return render(request, 'home/jobseeker.html',{'jobcreate':jobcreate})

def add_in_afterapply(request, pk):
	user=request.user
	resume=Resume.objects.get(user=user)
	job=get_object_or_404(Job, pk=pk)
	company_name=getattr(job,'company_name')
	location=getattr(job,'location')
	applied_by=request.user
	website=getattr(job,'website')
	title=getattr(job,'title')
	first_name=getattr(user,'first_name')
	last_name=getattr(user,'last_name')
	phoneNumber=getattr(resume,'phoneNumber')
	resume=getattr(resume,'resume')
	email=getattr(user,'email')
	job_created_by = getattr(job, 'user')
	afterapply.objects.create(user=user,title=title,companyname=company_name,location=location,applied_by=applied_by,website=website)
	recive_job_applications.objects.create(user=user, first_name=first_name,last_name=last_name,phone_number=phoneNumber,resume=resume,email=email,applied_by=applied_by,job_created_by=job_created_by)
	return redirect('home:index')


def after_apply(request):
	apply=afterapply.objects.filter(user=request.user)
	return render(request, 'home/afterapply.html',{'apply':apply})


# def recivejobapplications(request):
# 	recivejob=recive_job_applications.objects.all()
# 	return render(request, 'home/recive_job_applications.html',{'recivejob':recivejob})



#for search
def search(request):
	title = request.POST.get('title')
	location = request.POST.get('location')
	job = Job.objects.filter(location=location, title=title)
	return render(request,"home/index.html",{'job':job})

	

def recivejobapplications(request):
    recivejob = recive_job_applications.objects.filter( job_created_by=request.user)
    return render(request, 'home/recive_job_applications.html',{'recivejob':recivejob})
	
def update_status(request, pk):
    recieve = recive_job_applications.objects.filter(pk=pk)
    recievee = recive_job_applications.objects.get(pk=pk) #help .get for getattr() and .filter for update()
    applied_by = getattr(recievee, "applied_by")
    apply = afterapply.objects.filter(applied_by=applied_by)
    if request.method == 'POST':
        status = request.POST['status']
        if status=='Accept':
            recieve.update(status="Accepted!")
            apply.update(status="Accepted!")
        else:
            recieve.update(status="Rejected!")
            apply.update(status="Rejected!")

    return redirect("home:recivejobapplications")
