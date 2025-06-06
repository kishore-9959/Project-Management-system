from django.urls import path
from . import views

urlpatterns = [
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('task_dashboard/', views.task_dashboard, name='task_dashboard'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # User management views
    path('user_list_admin/', views.user_list_admin, name='user_list_admin'),
    path('user_list_user/', views.user_list_user, name='user_list_user'),
    path('add_user/', views.add_user, name='add_user'),
    path('update_user/<int:pk>/', views.update_user, name='update_user'),
    path('delete_user/<int:pk>/', views.delete_user, name='delete_user'),

    # Task management views
    
    path('task_list/', views.task_list, name='task_list'),
    path('get_filtered_milestones/', views.get_filtered_milestones, name='get_filtered_milestones'),
    path('create_task/', views.create_task, name='create_task'),
    path('update_task/<int:id>/', views.update_task, name='update_task'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),
]
