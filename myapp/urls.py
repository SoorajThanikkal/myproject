from django.urls import path
from . import views

urlpatterns = [
    # path('add/', views.add_place, name='add_place'),
    path('', views.exam, name='scan_folder'),
    path('congrats', views.congrats, name='congrats'),
    path('Save_image/', views.Save_image, name='Save_image'),

]
