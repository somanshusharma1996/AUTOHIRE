

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
# class Company(models.Model):
#     user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
#     name=models.CharField(max_length=200,null=True)
#     position=models.CharField(max_length=200,null=True)
#     description=models.CharField(max_length=2000,null=True)
#     salary=models.IntegerField(null=True)
#     experience=models.IntegerField(null=True)
#     Location=models.CharField(max_length=2000,null=True)
#     def __str__(self):
#         return self.name
#     # class meta:
#     #     verbose_name = 'Company'
#     #     verbose_name_plural = 'companies'


# class Candidates(models.Model):
#     category=(
#         ('Male','male'),
#         ('Female','female'),
#         ('Other','other'),
#     )
#     name=models.CharField(max_length=200,null=True)
#     dob=models.DateField(null=True)
#     gender= models.CharField(max_length=200,null=True,choices=category)
#     mobile= models.CharField(max_length=200,null=True)
#     email= models.CharField(max_length=200,null=True)
#     resume=models.FileField(null=True)
#     company=models.ManyToManyField(Company,blank=True)
#     def __str__(self):
#         return self.name



class Job(models.Model):
    JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=150)
    type = models.CharField(choices=JOB_TYPE, max_length=10)
    category = models.CharField(max_length=100)
    last_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    company_description = models.CharField(max_length=300)
    website = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(default=timezone.now)
    filled = models.BooleanField(default=False)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # slug = models.SlugField(default="user",null=True,blank=True)

    def get_absolute_url(self): # new
        return reverse('home:job_detail', kwargs={"pk": self.pk})

    


class Resume(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100,null=True,blank=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)

    
class afterapply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    companyname= models.CharField(max_length=100)
    website = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=150)
    applied_by=models.CharField(max_length=100,null=True)
    status= models.CharField(max_length=20,null=True,blank=True)

    def get_absolute_url(self):
        return reverse("home:afterapply", kwargs={'pk': self.pk})
    

class recive_job_applications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    resume = models.FileField(max_length=200)
    status = models.CharField(max_length=20, null=True, blank=True)
    applied_by=models.CharField(max_length=200, null=True)
    job_created_by = models.CharField(max_length=200, null=True)
    def get_absolute_url(self):
        return reverse("home:recivejobapplications", kwargs={'pk': self.pk})


