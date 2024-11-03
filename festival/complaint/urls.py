from django.urls import path
from . import views
urlpatterns=[
    # path('inbox',views.inbox_int),
    path('add_complaint/<int:art_dec>',views.add_complaint),
    path('viewcomplaints/<int:art_dec>',views.viewcomplaints),
    path('reply/<int:id>',views.reply)


]