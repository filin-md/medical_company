from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, UserUpdateView, generate_new_password, verification_view

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword', generate_new_password, name='generate_new_password'),

    path('verification/<str:token>', verification_view, name='verification'),

]