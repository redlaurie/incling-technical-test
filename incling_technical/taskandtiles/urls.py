from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/<str:pk>/', views.taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='task-delete'),
    path('tile-list/', views.tileList, name='tile-list'),
    path('tile-create/', views.tileCreate, name='tile-create'),
    path('tile-delete/<str:pk>/', views.tileDelete, name='tile-delete'),
    path('tile-update/<str:pk>/', views.tileUpdate, name='tile-update'),
]