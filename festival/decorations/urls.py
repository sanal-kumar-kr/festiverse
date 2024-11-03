from django.urls import path
from . import views
urlpatterns=[
    path('add_dec/<int:uid>',views.add_dec),
    path('view_dec/<int:uid>',views.view_dec),
    # path('decbookings/<int:uid>',views.decbookings),
    path('deletedecoration/<int:id>',views.deletedecoration),
    path('editdecoration/<int:id>',views.editdecoration),
    path('decoration_detail/<int:id>',views.decoration_detail)


]