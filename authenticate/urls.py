from django.urls import path, include
from . import views

app_name = 'auth_app'
urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('signOut/', views.signOut, name='logout'),
    path('sudo/', views.superUserDo, name='sudo'),
]