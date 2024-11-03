from django.urls import path
from . import views

urlpatterns = [
 
    path('usersreq/<int:ut>/',views.usersreq),
    path('users/<int:ut>/',views.users),
    path('decision/<int:uid>/<int:dec>',views.decision),
    path('edituser/<int:uid>',views.edituser),
    path('editart/<int:uid>',views.editart),
    path('editdec/<int:uid>',views.editdec),

    path('deleteuser/<int:uid>',views.deleteuser),
    # path('Search_user/<int:ut>',views.Search_user),

]