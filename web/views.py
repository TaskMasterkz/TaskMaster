from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import TaskSubmissionForm
from django.contrib.auth.decorators import login_required
from .models import Feedback
import io
import networkx as nx
import matplotlib.pyplot as plt
from django.http import HttpResponse


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



def networkx_graph_view(request):
    G = nx.DiGraph()
    G.add_edge("A", "B")
    G.add_edge("B", "C")
    G.add_edge("C", "A")

    plt.figure(figsize=(5, 5))
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, font_size=16, arrows=True)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)

    return HttpResponse(buf.getvalue(), content_type='image/png')
