from django.urls import path
from . import views
from .views import (
    IdentityUpdateView,
    QualificationsCreateView,
    ExperienceCreateView,
    InternshipCreateView,
    CertificationsCreateView,
    ProjectsCreateView,
    Technical_skillsCreateView,
)

app_name = 'resume'
urlpatterns = [
    path('resume/',views.resume, name='resume'),
    path('view_info/<int:pk>', IdentityUpdateView.as_view(), name='view_info'),
    path('view-qualification_form/', QualificationsCreateView.as_view(), name='view-qualification_form' ),
    path('experience/', ExperienceCreateView.as_view(), name='experience' ),
    path('internship/', InternshipCreateView.as_view(), name='internship'),
    path('certification/', CertificationsCreateView.as_view(), name='certification'),
    path('projects/', ProjectsCreateView.as_view(), name='projects'),
    path('skills/', Technical_skillsCreateView.as_view(), name='skills'),

]