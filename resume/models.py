from django.db import models
from django.db.models.base import Model
from home.models import User
from django.shortcuts import reverse
# Create your models here.
class Identity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # personal information
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=13, null=True)
    address = models.CharField(max_length=300, null=True)
    
    def get_absolute_url(self):
        return reverse("create_resume:resume", kwargs={"pk": self.pk})
    
    def get_update_identity_url(self):
        return reverse("create_resume:update-identity", kwargs={'pk': self.pk})
    
    
# Experience
class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    duration = models.CharField(max_length=100, null=False)
    desc = models.TextField(null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("resume:resume", kwargs={})

# Internship    
class Internship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name  = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200, null=True)
    duration = models.CharField(null=False, max_length=100)
    location = models.CharField(max_length=200, null=True)
    desc = models.TextField(null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("resume:resume", kwargs={})

# Qulaifications

class Qualifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=200, null=True)
    degree = models.CharField(max_length=100, null=True)
    branch = models.CharField(max_length=200, null=True)
    duration = models.CharField(null=False, max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("resume:resume")
    
# Certifications
class Certifications(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE) 
   name = models.CharField(max_length=200, null=True)
   company = models.CharField(max_length=200, null=True)
   duration = models.CharField(null=False, max_length=100)
   desc = models.TextField(null=True, blank=True)
   
   def get_absolute_url(self):
       return reverse("resume:resume", kwargs={})
   
    

# Projects
class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    duration = models.CharField(null=False, max_length=100)
    desc = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("resume:resume", kwargs={})
    
# skills
class Technical_skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=200, null=True)
    expertise = models.CharField(max_length=100, null=True)  
    
    def get_absolute_url(self):
        return reverse("resume:resume", kwargs={}) 
   
