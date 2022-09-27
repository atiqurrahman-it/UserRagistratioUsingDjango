from django.urls import path

from . import views

urlpatterns = [
    
    path('',views.SingUp,name='ragistration'),
    path('login/',views.Login,name='login'),
    path('logout/',views.LogOut,name='logout'),
    path('dashboard/',views.Dashboard,name='dashboard')
]
