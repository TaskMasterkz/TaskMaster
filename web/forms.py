from django import forms

class TaskSubmissionForm(forms.Form):
    name = forms.CharField(label="Аты-жөніңіз", max_length=100, widget=forms.TextInput(attrs={'class': 'input-field'}))
    description = forms.CharField(label="Тапсырма сипаттамасы", widget=forms.Textarea(attrs={'class': 'input-field'}))
    file = forms.FileField(label="Файл жүктеу", required=False)
