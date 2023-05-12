# MEMBUAT APLIKASI ECOMMERCE E-SHOPPER MENGGUNAKAN DJANGO V3.2

[Submber:](https://www.youtube.com/@CodingEx)


#### 1. Membuat virtual environment

        new file:   .gitignore
        new file:   README.md

        > python -m venv venv3932


#### 2. Menginstall django v3.2

        new file:   .gitignore
        new file:   README.md

        > venv3932\Scripts\activate
        > pip install django==3.2.*
        ...
         Downloading Django-3.2.19-py3-none-any.whl (7.9 MB)


#### 3. Meng-upgrade pip

        new file:   .gitignore
        new file:   README.md

        > python.exe -m pip install --upgrade pip
        ...
        Successfully installed pip-23.1.2


#### 4. Memeriksa hasil instalasi

        new file:   .gitignore
        new file:   README.md

        > pip list
        
        Package    Version
        ---------- -------
        asgiref    3.6.0
        Django     3.2.19
        pip        23.1.2
        pytz       2023.3
        setuptools 56.0.0
        sqlparse   0.4.4


#### 5. Membuat django proyek dengan nama'config'

        > django-admin startproject config .
        ...
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 6. Membuat django app dengan nama 'main'

        > mkdir app
        > mkdir app\main
        > django-admin startapp main app\main
        ...
        new file:   app/main/__init__.py
        new file:   app/main/admin.py
        new file:   app/main/apps.py
        new file:   app/main/migrations/__init__.py
        new file:   app/main/models.py
        new file:   app/main/tests.py
        new file:   app/main/views.py


#### 7. Register main app pada proyek config

        modified:   .gitignore
        modified:   README.md
        modified:   app/main/apps.py
        modified:   config/settings.py


#### 8. Menjalankan django lokal server dan menampilkan django pada web browser

        > python manage.py runserver
        > http://127.0.0.1:8000/


