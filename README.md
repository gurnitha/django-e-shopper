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


#### 9. Membuat halo world

        modified:   README.md
        new file:   app/main/urls.py
        modified:   app/main/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/app/main/index.html

        : 'DIRS': ['templates'],


#### 10. Mengisi html template pada home page

        modified:   README.md
        modified:   templates/app/main/index.html


#### 11. Mengisi assets (css,js,images,fonts)

        modified:   .gitignore
        modified:   README.md

        : static


#### 12. Membuat path untuk static_root dan staticfiles_dir

        modified:   README.md
        modified:   config/settings.py

        : STATIC_URL  = '/static/'
        : STATIC_ROOT = '/static/'
        : STATICFILES_DIRS = [
        	os.path.join(BASE_DIR, 'static')
          ]


#### 13. Loding static files

        modified:   README.md
        modified:   config/settings.py

        : STATIC_URL  = '/static/'
        : STATIC_ROOT = '/static/'
        : STATICFILES_DIRS = [
        	os.path.join(BASE_DIR, 'static')
          ]


#### 14. Membuat base.html file

        modified:   README.md
        modified:   templates/app/main/index.html
        new file:   templates/base.html


#### 15. Memindahkan html template dari index.html ke base.html

        modified:   README.md
        modified:   templates/app/main/index.html
        new file:   templates/base.html


#### 16. Meng-extends base.html ke index.html

        modified:   README.md
        modified:   templates/app/main/index.html


#### 17. Men-sagmentasi base.html template dan template inheritance

        modified:   README.md
        new file:   templates/app/main/components/content.html
        new file:   templates/app/main/components/slider.html
        modified:   templates/app/main/index.html
        modified:   templates/base.html
        new file:   templates/partials/_footer.html
        new file:   templates/partials/_header.html
        new file:   templates/partials/_scripts.html


#### 18. Men-sagmentasi content index.html

        modified:   README.md
        new file:   templates/app/main/components/brands_products.html
        new file:   templates/app/main/components/category_products.html
        new file:   templates/app/main/components/category_tab.html
        deleted:    templates/app/main/components/content.html
        new file:   templates/app/main/components/features_items.html
        new file:   templates/app/main/components/price_range.html
        new file:   templates/app/main/components/recommended_items.html
        new file:   templates/app/main/components/shipping.html
        modified:   templates/app/main/index.html
        modified:   templates/base.html


#### 19. Membuat page title

        modified:   README.md
        modified:   templates/app/main/index.html
        modified:   templates/base.html


#### 20. Database - Create MySQL database

        λ mysql -u root -p
        Enter password: ****

        ...
        mysql> CREATE DATABASE django_e_shopper_multivendor;
        Query OK, 1 row affected (0.04 sec)

        mysql> USE django_e_shopper_multivendor;
        Database changed


#### 20. Database - Instal MySQL driver untuk Django

        > pip install mysqlclient