from django.urls import path, include
from . import views

app_name = 'base_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('addStudent/', views.addStudent, name='add'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('modify/<str:pk>/', views.modify, name='modify'),
]