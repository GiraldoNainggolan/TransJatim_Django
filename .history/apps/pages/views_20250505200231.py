from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # Misal ini list contoh, nanti bisa kamu ganti sesuai kebutuhan
    some_python_list = ['name', 'email', 'date']

    context = {
        'db_filters': some_python_list,
        'segment': 'dashboard'
    }

    # Page from the theme 
    return render(request, 'pages/index.html', context)
