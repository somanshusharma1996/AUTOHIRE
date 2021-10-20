from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import DeleteView, UpdateView

from home.models import Resume
from .models import *

# Create your views here.

def resume(request):
    user = request.user
    resume = Resume.objects.get(user=user)
    qualifications = Qualifications.objects.filter(user=user)
    experience = Experience.objects.filter(user=user)
    internship = Internship.objects.filter(user=user)
    certification = Certifications.objects.filter(user=user)
    project = Projects.objects.filter(user=user)
    technical_skill = Technical_skills.objects.filter(user=user)
    context = {
        'user':user,
        'resume':resume,
        'qualifications':qualifications,
        'experience':experience,
        'internship':internship,
        'certification':certification,
        'project':project,
        'technical_skill':technical_skill,
    }

    
    return render(request, 'resume/view_resume.html', context)

class IdentityUpdateView( UpdateView):
    model = Identity
    fields = ['name', 'email', 'phone_number', 'address']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        identity = self.get_object()
        if self.request.user == identity.user:
            return True
        return False

    
class ExperienceCreateView(CreateView):
    model = Experience
    fields = ['name', 'position', 'location', 'duration', 'desc']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class InternshipCreateView(CreateView):
    model = Internship
    fields = ['name', 'position', 'location', 'duration', 'desc']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class QualificationsCreateView(CreateView):
    model = Qualifications
    fields = ['name', 'location', 'degree', 'branch', 'duration']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CertificationsCreateView(CreateView):
    model = Certifications
    fields = ['name', 'company', 'duration', 'desc']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectsCreateView(CreateView):
    model = Projects
    fields = ['name', 'duration', 'desc', 'link']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Technical_skillsCreateView(CreateView):
    model = Technical_skills
    fields = ['skill', 'expertise']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


   
    
    
    
    
    
