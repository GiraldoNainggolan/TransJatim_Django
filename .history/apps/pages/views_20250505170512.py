from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
context = {
        'db_filters': some_python_list,  # ← problem di sini!
    }
    # Page from the theme 
    return render(request, 'pages/index.html', {'segment': 'dashboard'})
