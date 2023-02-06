from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count
from .models import Trailer, Package

# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def index(request):
    if request.method == 'POST':
        input_text = request.POST.get('inputText')
        trailers = Trailer.objects.filter(id=input_text)
        result = []
        for trailer in trailers:
            packages = Package.objects.filter(trailer_id=trailer.id)
            total_count = packages.count()
            for package in packages.values('destination_lane').annotate(destination_count=Count('destination_lane')):
                percentage = round(package['destination_count'] * 100.0 / total_count, 2)
                result.append({
                    "destination_lane": package['destination_lane'],
                    "percentage": percentage,
                })
        return render(request, "main/base.html", {"result": result})
    return render(request, 'main/base.html')



