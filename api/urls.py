from django.urls import path

from . import views


urlpatterns = [
    path('todo/', views.task_list, name='task_list'),
    path('todo/<int:pk>/', views.task_detail, name='task_detail'),
    path('todo/<int:pk>/execute/', views.task_execute, name='task_execute'),
]
