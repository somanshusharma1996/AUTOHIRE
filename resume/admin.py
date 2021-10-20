from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(Identity)

class qulaifications(admin.ModelAdmin):
    list_display = ('id',)
admin.site.register(Qualifications, qulaifications)

admin.site.register(Experience)
admin.site.register(Internship)
admin.site.register(Certifications)
admin.site.register(Projects)
admin.site.register(Technical_skills)


