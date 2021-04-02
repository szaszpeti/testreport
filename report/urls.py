from django.urls import path

from django.contrib.auth import views as auth_views

from . import views



urlpatterns = [

    path('', views.home, name="home"),
    path('prework', views.prework, name="prework"),
    

    path('inspection_detail/<str:pk>', views.inspectionDetail, name="inspection_detail"),
    path('blade_detail/<str:pk>', views.bladeDetail, name="blade_detail"),

    path('create_operation', views.createOperation, name="create_operation"),
    path('create_blade/<str:pk>', views.createBlade, name="create_blade"),
    path('create_inspection/<str:pk>', views.createInspection, name="create_inspection"),
    
    path('delete_operation/<str:pk>', views.deleteOperation, name="delete_operation"),
    path('delete_blade/<str:pk>', views.deleteBlade, name="delete_blade"),
    path('delete_inspection/<str:pk>', views.deleteInspection, name="delete_inspection"),
  
  	path('update_operation/<str:pk>', views.updateOperation, name="update_operation"),
    path('update_blade/<str:pk>', views.updateBlade, name="update_blade"),
    path('update_inspection/<str:pk>', views.updateInspection, name="update_inspection"),
  

   

]