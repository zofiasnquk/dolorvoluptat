# views.py
from django.shortcuts import render

def show_route(request):
    context = {
        'route': {'name': 'home'}
    }
    return render(request, 'example_template.html', context)
