from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name="Аты-жөні")
    description = models.TextField(verbose_name="Тапсырма сипаттамасы")
    file = models.FileField(upload_to="orders/", blank=True, null=True, verbose_name="Қосымша файл")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Жіберілген уақыт")

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"


# 1. Тапсырыстар кестесі
class Task(models.Model):
    name = models.CharField(max_length=255, default='No name')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пайдаланушы
    title = models.CharField(max_length=255)  # Тапсырыстың атауы
    description = models.TextField()  # Толық сипаттамасы
    file = models.FileField(upload_to="tasks/", blank=True, null=True)  # Файл жүктеу
    created_at = models.DateTimeField(auto_now_add=True)  # Қашан жіберілді
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Күтуде'),
        ('in_progress', 'Орындауда'),
        ('completed', 'Аяқталды')
    ], default='pending')  # Күйі (статус)

    def __str__(self):
        return self.title

# 2. Пайдаланушылардың бағалау кестесі
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пайдаланушы
    rating = models.IntegerField()  # Баға (1-5)
    comment = models.TextField()  # Пікір мәтіні
    created_at = models.DateTimeField(auto_now_add=True)  # Автоматты түрде уақыты

    def __str__(self):
        return f"{self.user.username} - {self.rating}"

