from django.urls import path
from . import views

urlpatterns = [
    path('<int:stud_id>/details/', views.studDetails, name='studdetails'),
    path('browse/', views.browse, name='browse'),
    path('addstud/', views.addstud, name='addstud'),
    path('returnstud/', views.returnstud, name='returnstud'),
    path('<int:stud_id>/delete/', views.deletestud, name="deletestud"),
    path('<int:stud_id>/edit', views.editstud, name='editstud'),
    path('<int:stud_id>/depart', views.changeDepart, name='changeDepart'),
    path('<int:stud_id>/status', views.changeStatus, name='changeStatus')
]