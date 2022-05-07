from . import views
from django.urls import path

urlpatterns = [
    path('signup/',views.signupAction,name='signup'),
    path('login/',views.loginAction,name='login'),
]