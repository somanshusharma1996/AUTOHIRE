from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('candidate_signup/', views.candidate_signup_view, name="candidate_signup"),
    path('employer_signup/', views.employer_signup_view, name="employer_signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]