from django.urls import path
from django.contrib.auth import views as auth_views 
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('family_tree/', views.index, name='index'),
    path('individual/<int:person_id>/', views.get_individual2, name='individual'),
    path('name/', views.get_name, name='name'),
    path('register/', views.register, name='register'),
    #path('login/', views.login, name='login'),
    #path('logout/', views.logout, name='logout'),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    path('base/', views.base, name='base')
]