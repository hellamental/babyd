from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('individual/<int:person_id>/', views.get_individual2, name='individual'),
    path('name/', views.get_name, name='name')
]