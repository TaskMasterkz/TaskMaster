from django.shortcuts import render

def index(request):
    return render(request, 'web/index.html')

def price_list(request):
    return render(request, 'web/price.html')
