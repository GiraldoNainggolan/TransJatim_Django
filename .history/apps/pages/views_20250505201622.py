from django.shortcuts import render
import json

# Create your views here.

def index(request):
    # Contoh data, nanti bisa diisi dari database atau sesuai kebutuhanmu
    some_python_list = ['name', 'email', 'date', 'phone']

    context = {
        'db_filters': json.dumps(some_python_list),  # pastikan dikonversi ke JSON agar JS paham
        'segment': 'dashboard'
    }

    # Render halaman dengan context
    return render(request, 'pages/index.html', context)
