from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def search(request):
    if request.method == 'POST':
        input_text = request.POST.get('inputText')
        # Perform database query using input_text as a parameter
        # ...
        return HttpResponse('Query results')
    return render(request, 'base.html')
