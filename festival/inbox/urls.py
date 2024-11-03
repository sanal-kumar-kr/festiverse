from django.urls import path
from . import views
urlpatterns=[
    path('inbox',views.inbox_int),
    path('message/<int:ptwoid>',views.message)
]