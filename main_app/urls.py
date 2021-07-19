from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hikers/', views.hikers_index, name='index'),
    path('hikers/<int:hiker_id>/', views.hikers_detail, name='detail'), 
    path('hikers/create/', views.HikerCreate.as_view(), name='hikers_create'),
    path('hikers/<int:pk>/update/', views.HikerUpdate.as_view(), name='hikers_update'),
    path('hikers/<int:pk>/delete/', views.HikerDelete.as_view(), name='hikers_delete'),
    path('hikers/<int:hiker_id>/assoc_gear/<int:gear_id>/', views.assoc_gear, name='assoc_gear'), 
]


