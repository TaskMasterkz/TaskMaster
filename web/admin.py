from django.contrib import admin
from .models import Task, Feedback

class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'status', 'created_at')
    search_fields = ('user__username', 'title')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'comment', 'created_at')
    search_fields = ('user__username', 'rating')

admin.site.register(Task, TaskAdmin)
admin.site.register(Feedback, FeedbackAdmin)
