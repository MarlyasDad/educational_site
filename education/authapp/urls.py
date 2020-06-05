from django.urls import path

from . import views

app_name = 'authapp'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.UserDetailView.as_view(), name='user_profile'),
]
