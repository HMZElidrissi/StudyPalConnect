from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),
    path('logout/', views.logout_user, name="logout"),
    path('', views.home, name="home"),
    path('profile/<str:pk>', views.user_profile, name='profile'),
    path('room/<str:pk>', views.room, name='room'),
    path('create-room/', views.create_room, name='create-room'),
    path('update-room/<str:pk>', views.update_room, name='update_room'),
    path('delete-room/<str:pk>', views.delete_room, name='delete_room'),
    path('delete-message/<str:pk>', views.delete_message, name='delete_message'),
    path('update-user/', views.update_user, name='update_user'),
    path('topics/', views.topics_page, name='topics'),
    path('activities/', views.activities_page, name='activities')
]
