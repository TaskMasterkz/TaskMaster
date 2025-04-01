from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('submit_task/', views.submit_task, name='submit_task'),
    path('reviews/', views.reviews, name='reviews'),
    path('contact/', views.contact, name='contact'),
    path('submit-task/', views.submit_task, name='submit_task'),
    path('task-success/', views.task_success, name='task_success'),
]
