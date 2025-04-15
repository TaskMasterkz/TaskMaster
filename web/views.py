from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import TaskSubmissionForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Feedback

def home(request):
    feedbacks = Feedback.objects.order_by('-created_at')[:5]
    return render(request, 'web/home.html', {'feedbacks': feedbacks})

def pricing(request):
    return render(request, 'web/pricing.html')

@login_required
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

@login_required
def reviews(request):
    return render(request, 'web/reviews.html')

def contact(request):
    return render(request, 'web/contact.html')

@login_required
def task_success(request):
    return render(request, 'web/task_success.html')

@login_required
def give_feedback(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        if request.user.is_authenticated:
            Feedback.objects.create(user=request.user, rating=rating, comment=comment)
            return redirect('home')  # Немесе 'feedback_success'
        else:
            return redirect('login')
    return render(request, 'web/feedback.html')


from graphviz import Digraph
from django.http import HttpResponse

def graph_view(request):
    # Graphviz графикасын құру
    dot = Digraph(comment='The Round Table')
    dot.node('A', 'King Arthur')
    dot.node('B', 'Lancelot')
    dot.edge('A', 'B', 'Knows')

    # Графикті PNG ретінде қайтару
    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = 'inline; filename="graph.png"'
    response.write(dot.pipe(format='png'))

    return response
