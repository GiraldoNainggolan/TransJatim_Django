Step | Perintah | Keterangan
1 | mkdir transjatim_sentiment | Buat folder project
2 | cd transjatim_sentiment | Masuk ke folder
3 | python -m venv env | Buat virtual environment
4 | .\env\Scripts\Activate.ps1 | Aktifkan env
5 | pip install django | Install Django
6 | django-admin startproject transjatim_sentiment . | (Ingat ada titik . di akhir!)
7 | python manage.py startapp dashboard | Buat app pertama
8 | python manage.py startapp sentiment | Buat app kedua
9 | python manage.py startapp users | Buat app ketiga
10 | Tambahkan semua app ke INSTALLED_APPS di settings.py | 
11 | Buat urls.py di tiap app (kalau belum ada) | 
12 | Setting static/ dan templates/ di settings.py | 
13 | Jalankan python manage.py makemigrations | 
14 | Jalankan python manage.py migrate | 
15 | Jalankan server python manage.py runserver | 🚀

 python -m certifi

python manage.py createsuperuser

Username: giraldo
Email address: giraldo@gmail.com
Password: giraldo

untuk menjalan kan python sentimen.py

D:\Freelance\Dela\Project\Django\transjatim_sentiment\env\lib\site-packages\certifi\cacert.pem


bareer token: AAAAAAAAAAAAAAAAAAAAACRt0wEAAAAAAKGhOh4SIavEMsFscGlLnBndP4I%3DwCwL7Ipefqc58FXyDLCAppNbU4yL351sWyzLL5VIJVfFCDNbiL

API Key : z9kaNwIDmuqB2Tm8jFmoeen1Z

API Key Secret : sPHotKwijrYzrPzB9ZBb9U8TgidJoJyveT1E0AdIhotyCV6wXG

Access Token : 1627833245885935616-WRiwrmTpCTxh6FAhthoNcabIeMHUjh

Access Token Secret : yof5RTRmyJk5cdjYSNOv3oRNmlTfducqPMdSlBxuy1VuX