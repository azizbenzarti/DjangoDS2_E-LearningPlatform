from django.urls import re_path

from . import views

urlpatterns = [
    # re_path('signup',  views.registration_view, name='register'),
    re_path('login', views.login,name='login'),
    re_path('test_token', views.test_token),
]
