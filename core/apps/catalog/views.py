from django.shortcuts import render


def index(request):
    data = {
        'Title': 'Основная',
        'Message': 'Привет!'
    }
    return render(request, 'index.html', data)
