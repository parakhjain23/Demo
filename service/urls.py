from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('details/',views.details,name='details'),
    
]