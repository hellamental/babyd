from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('individual/<int:person_id>/', views.individual, name='individual'),
    path('name/', views.get_name, name='name')
]