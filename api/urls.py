from django.urls import path
from . import views

urlpatterns = [
    path('submit_task/', views.SubmitTaskView.as_view(), name='submit_task_api'),
    path('reviews/', views.ReviewListCreateView.as_view(), name='reviews_api'),
]
