from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):  # New view for the root URL
    return render(request, 'index.html')
