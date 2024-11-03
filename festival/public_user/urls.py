from django.urls import path
from . import views

urlpatterns = [
 
    
    path('Search_user/<int:ut>',views.Search_user),
    path('add_feedback/<int:uid>',views.add_feedback),
    path('viewfeedbacks/<int:uid>',views.view_feedbacks),
    path('deletefeedback/<int:fid>',views.deletefeedback),


]