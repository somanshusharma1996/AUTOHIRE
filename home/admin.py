from django.contrib import admin
from .models import Resume,Job, afterapply,recive_job_applications
# Register your models here.
class job(admin.ModelAdmin):
    list_display = ('id','user','title','description','location','type','category','last_date','company_name','company_description','website','created_at')
admin.site.register(Job,job)

admin.site.register(Resume)
admin.site.register(afterapply)
admin.site.register(recive_job_applications)