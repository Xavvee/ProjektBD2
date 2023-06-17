from django.urls import path
from .views import create_client, create_dish, create_game, create_employee, find_client, delete_client, find_dish, \
    delete_dish, find_game, delete_game, find_employee, delete_employee, update_client, update_dish, update_game, \
    update_employee, find_all_clients, find_all_games, find_all_employees, find_all_dishes, create_reservation , find_client_reservations, \
    find_future_client_reservations, find_past_client_reservations, find_reservation_with_status

urlpatterns = [
    path('create_client/', create_client, name='create_client'),
    path('create_dish/', create_dish, name='create_dish'),
    path('create_game/', create_game, name='create_game'),
    path('create_employee/', create_employee, name='create_employee'),
    path('create_reservation/', create_reservation, name='create_reservation'),
    path('find_client/', find_client, name='find_client'),
    path('delete_client/', delete_client, name='delete_client'),
    path('find_dish/', find_dish, name='find_dish'),
    path('delete_dish/', delete_dish, name='delete_dish'),
    path('find_game/', find_game, name='find_game'),
    path('delete_game/', delete_game, name='delete_game'),
    path('find_employee/', find_employee, name='find_employee'),
    path('delete_employee/', delete_employee, name='delete_employee'),
    path('update_client/', update_client, name='update_client'),
    path('update_dish/', update_dish, name='update_dish'),
    path('update_game/', update_game, name='update_game'),
    path('update_employee/', update_employee, name='update_employee'),
    path('find_all_clients/', find_all_clients, name='find_all_clients'),
    path('find_all_games/', find_all_games, name='find_all_games'),
    path('find_all_employees/', find_all_employees, name='find_all_employees'),
    path('find_all_dishes/', find_all_dishes, name='find_all_dishes'),
    path('find_client_reservations/', find_client_reservations, name='find_client_reservations'),
    path('find_future_client_reservations/', find_future_client_reservations, name='find_future_client_reservations'),
    path('find_past_client_reservations/', find_past_client_reservations, name='find_past_client_reservations'),
    path('find_reservation_with_status/', find_reservation_with_status, name='find_reservation_with_status')
]
