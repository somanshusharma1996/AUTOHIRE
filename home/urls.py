from django.urls import path
from . import views
from . views import (JobCreateView,recivejobapplications,search)
app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('job_detail/<int:pk>', views.job_detail, name='job_detail'),
    path('job/', JobCreateView.as_view(), name='job'),
    path('jobseeker/', views.job_create_list, name='job_create_list'),
    path('afterapply/<int:pk>', views.add_in_afterapply, name='afterapply'),
    path('afterapply/', views.after_apply, name='after_apply'),
    path('recive_job_applications/',views.recivejobapplications,name='recivejobapplications'),
    path('search/',views.search, name='search'),
    path('update_status/<int:pk>', views.update_status, name='update_status'),
    path('media/<int:pk>', views.open_resume, name='open_resume')
    
]