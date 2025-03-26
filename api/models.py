from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('simple', 'Простая'),
        ('explanation', 'С объяснением'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
