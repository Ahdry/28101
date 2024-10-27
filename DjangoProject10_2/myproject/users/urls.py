from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_users, name='register_users'),
    path('list/', views.list_users, name='list_users'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('detail/<int:user_id>/', views.user_detail, name='user_detail'),
]