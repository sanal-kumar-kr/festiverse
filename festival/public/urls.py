from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('service',views.service),
    path('contact',views.contact),
    path('login',views.Login),
    path('organizersreg',views.organizersreg),
    path('vendorsreg',views.vendorsreg),
    path('artistsreg',views.artistsreg),
    path('usersreg',views.usersreg),
    path('myprofile/<int:uid>',views.myprofile),
    path('la',views.la),
    path('logout',views.Logout)
   
]