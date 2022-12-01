from django.urls import path

from . import views

urlpatterns = [

    path("", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("register/", views.register_request, name="register"),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('social/signup/', views.signup_redirect, name='signup_redirect'),

]
