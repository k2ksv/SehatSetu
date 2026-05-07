from django.urls import path
from . import views

urlpatterns = [
    path('api/auth/register/', views.register, name='register'),
    path('api/auth/login/', views.login_view, name='login'),
    path('api/auth/logout/', views.logout_view, name='logout'),
    path('api/auth/current-user/', views.get_current_user, name='current_user'),
    path('api/users/', views.users_list, name='users_list'),
    path('api/users/<int:user_id>/', views.get_user_by_id, name='get_user'),
    path('api/users/<int:user_id>/update/', views.update_user_profile, name='update_user'),
]
