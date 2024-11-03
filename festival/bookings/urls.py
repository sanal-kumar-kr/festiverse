from django.urls import path
from . import views

urlpatterns = [
 
    path('bookuser/<int:fuid>',views.bookuser),
    path('bookpro/<int:fuid>',views.bookpro),
    path('view_dpro/<int:uid>',views.view_dpro),
    path('delete_program/<int:id>',views.delete_program),
    path('view_bookings/<int:id>',views.view_bookings),
    path('edit_program/<int:id>',views.edit_program),
    path('add_programs/<int:id>',views.add_programs),
    path('cancelbook/<int:id>',views.cancelbook),
    path('view_prg/<int:id>',views.view_prg),

    # path('viewbookings',views.viewbookings),

    

]