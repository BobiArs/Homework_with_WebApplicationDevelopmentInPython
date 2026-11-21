from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def news(request, subpath=None):
    return render(request, 'main/news.html')

def management(request, subpath=None):
    return render(request, 'main/management.html')

def facts(request, subpath=None):
    return render(request, 'main/facts.html')

def contacts(request, subpath=None):
    return render(request, 'main/contacts.html')

def history(request, subpath=None):
    return render(request, 'main/history.html')

def history_people(request):
    return render(request, 'main/history_people.html')

def history_photos(request):
    return render(request, 'main/history_photos.html')