from django.urls import path
from . import views
urlpatterns=[
    path('add_events',views.add_events)
]