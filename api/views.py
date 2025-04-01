from rest_framework import generics
from .models import Task, Review
from .serializers import TaskSerializer, ReviewSerializer

class SubmitTaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
