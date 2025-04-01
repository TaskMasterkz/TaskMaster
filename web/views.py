from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import TaskSubmissionForm

def home(request):
    return render(request, 'web/home.html')

def pricing(request):
    return render(request, 'web/pricing.html')

def submit_task(request):
    if request.method == "POST":
        form = TaskSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            file = request.FILES.get('file')  # Файлды аламыз

            # Email мәліметтері
            subject = f"Жаңа тапсырма: {name}"
            message = f"Аты-жөні: {name}\n\nСипаттама:\n{description}"

            email = EmailMessage(subject, message, 'your-email@example.com', ['your-email@example.com'])

            # Егер файл бар болса, хатқа тіркеу
            if file:
                email.attach(file.name, file.read(), file.content_type)

            email.send()

            return redirect('task_success')  # Жіберілгеннен кейін басқа бетке бағыттау

    else:
        form = TaskSubmissionForm()

    return render(request, 'web/submit_task.html', {'form': form})

def reviews(request):
    return render(request, 'web/reviews.html')

def contact(request):
    return render(request, 'web/contact.html')


def task_success(request):
    return render(request, 'web/task_success.html')