from django.urls import path
from .views import create_client, create_dish, create_game, create_employee, find_client, delete_client, find_dish, \
    delete_dish, find_game, delete_game, find_employee, delete_employee

urlpatterns = [
    path('create_client/', create_client, name='create_client'),
    path('create_reservation/', create_dish, name='create_reservation'),
    path('create_game/', create_game, name='create_game'),
    path('create_employee/', create_employee, name='create_employee'),
    path('find_client/', find_client, name='find_client'),
    path('delete_client/', delete_client, name='delete_client'),
    path('find_dish/', find_dish, name='find_dish'),
    path('delete_dish/', delete_dish, name='delete_dish'),
    path('find_game/', find_game, name='find_game'),
    path('delete_game/', delete_game, name='delete_game'),
    path('find_employee/', find_employee, name='find_employee'),
    path('delete_employee/', delete_employee, name='delete_employee'),
]
