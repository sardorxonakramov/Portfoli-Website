from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("contact/", views.ContactView, name="contact"),
    path("login/", LoginView.as_view(template_name="App_Users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('register/', views.UserRegistration.as_view(), name='register'),
     path('profile/', views.user_profile_view, name='user_profile'),
]
