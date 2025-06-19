from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

 
urlpatterns = [
    
    path('', views.home , name='home'),
    
    path('signup/',views.signup_view, name='signup'),
    path('login/', views.login_view , name='login'),
    path('logout/', views.logout_view , name='logout'),
    
    path('seeker/dashboard/', views.seeker_dashboard , name='seeker_dashboard'),
    path('employer/dashboard/', views.employer_dashboard, name ='employer_dashboard'),
    path('employer/post_job/', views.post_job , name='post_job'),
    path('jobs/', views.job_list , name='job_list'),
    
    

 ]
