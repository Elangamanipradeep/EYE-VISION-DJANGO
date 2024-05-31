from django.urls import path
from . import views

app_name = 'opticals'

urlpatterns = [
    path('', views.login_user, name='login'),
    path('index',views.index , name='index'),
    path('logout/', views.logout_user, name='logout'), 
    path('register/', views.register, name='register'),
    path('careera/', views.careera, name='careera'), 
    path('TommyHillfiger/', views.TommyHillfiger, name='TommyHillfiger'), 
    path('Empario/', views.Empario, name='Empario'), 
    path('Rayban/', views.Rayban, name='Rayban'), 
    path('Fastrack/', views.Fastrack, name='Fastrack'), 
]