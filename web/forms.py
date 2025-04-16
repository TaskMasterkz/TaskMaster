from django import forms
from .models import Task

class TaskSubmissionForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'file']
        labels = {
            'name': 'Аты-жөніңіз',
            'description': 'Тапсырма сипаттамасы',
            'file': 'Файл жүктеу',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field'}),
            'description': forms.Textarea(attrs={'class': 'input-field'}),
        }
