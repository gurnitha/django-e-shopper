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


#### 21. Database - Membuat konfigurasi db pada django proyek

        DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'xx',
            'USER': 'xx',
            'PASSWORD': 'xx',
            'HOST':'localhost',
            'PORT':'3306',
            }
        }


#### 22. Admin - Membuat superuser

        > python manage.py makemigrations
        > python manage.py migrate
        ...
        Running migrations:
          Applying contenttypes.0001_initial... OK
          Applying auth.0001_initial... OK
          Applying admin.0001_initial... OK
          Applying admin.0002_logentry_remove_auto_add... OK
          Applying admin.0003_logentry_add_action_flag_choices... OK
          Applying contenttypes.0002_remove_content_type_name... OK
          Applying auth.0002_alter_permission_name_max_length... OK
          Applying auth.0003_alter_user_email_max_length... OK
          Applying auth.0004_alter_user_username_opts... OK
          Applying auth.0005_alter_user_last_login_null... OK
          Applying auth.0006_require_contenttypes_0002... OK
          Applying auth.0007_alter_validators_add_error_messages... OK
          Applying auth.0008_alter_user_username_max_length... OK
          Applying auth.0009_alter_user_last_name_max_length... OK
          Applying auth.0010_alter_group_name_max_length... OK
          Applying auth.0011_update_proxy_permissions... OK
          Applying auth.0012_alter_user_first_name_max_length... OK
          Applying sessions.0001_initial... OK

        > python manage.py createsuperuser

        Username (leave blank to use 'hp'): admin
        Email address: admin@admin.com
        Password: admin
        Password (again):
        The password is too similar to the username.
        This password is too short. It must contain at least 8 characters.
        This password is too common.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.


        mysql> USE django_e_shopper_multivendor;
        Database changed
        mysql> show tables;
        +----------------------------------------+
        | Tables_in_django_e_shopper_multivendor |
        +----------------------------------------+
        | auth_group                             |
        | auth_group_permissions                 |
        | auth_permission                        |
        | auth_user                              |
        | auth_user_groups                       |
        | auth_user_user_permissions             |
        | django_admin_log                       |
        | django_content_type                    |
        | django_migrations                      |
        | django_session                         |
        +----------------------------------------+
        10 rows in set (0.00 sec)

        mysql> DESC auth_user;
        +--------------+--------------+------+-----+---------+----------------+
        | Field        | Type         | Null | Key | Default | Extra          |
        +--------------+--------------+------+-----+---------+----------------+
        | id           | int(11)      | NO   | PRI | NULL    | auto_increment |
        | password     | varchar(128) | NO   |     | NULL    |                |
        | last_login   | datetime(6)  | YES  |     | NULL    |                |
        | is_superuser | tinyint(1)   | NO   |     | NULL    |                |
        | username     | varchar(150) | NO   | UNI | NULL    |                |
        | first_name   | varchar(150) | NO   |     | NULL    |                |
        | last_name    | varchar(150) | NO   |     | NULL    |                |
        | email        | varchar(254) | NO   |     | NULL    |                |
        | is_staff     | tinyint(1)   | NO   |     | NULL    |                |
        | is_active    | tinyint(1)   | NO   |     | NULL    |                |
        | date_joined  | datetime(6)  | NO   |     | NULL    |                |
        +--------------+--------------+------+-----+---------+----------------+
        11 rows in set (0.06 sec)

        mysql> SELECT username, email FROM auth_user;
        +----------+-----------------+
        | username | email           |
        +----------+-----------------+
        | admin    | admin@admin.com |
        +----------+-----------------+
        1 row in set (0.00 sec)


#### 23. Database - set up environment variables

        Langkah:

        1. > pip install django-environ

        2. Create your .env file

        3. Declare your environment variables in .env

        SECRET_KEY=xxx
        DATABASE_NAME=xxx
        DATABASE_USER=xx
        DATABASE_PASS=xx

        4. Import environ in settings.py
        
        import environ

        5. Initialise environ
        # Initialise environment variables
        env = environ.Env(
            # set casting, default value
            # DEBUG=(bool, False)
            DEBUG=(bool, True)
        )

        5. Replace all references to your environment variables in settings.py

        # Take environment variables from .env file
        environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

        # Secret_key
        SECRET_KEY = env('SECRET_KEY')

        # Database
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': env('DATABASE_NAME'),
                'USER': env('DATABASE_USER'),
                'PASSWORD': env('DATABASE_PASS'),
            }
        }

        6. IMPORTANT: Add your .env file to .gitignore

        7. Run server for testing

        System check identified no issues (0 silenced).
        May 12, 2023 - 11:12:11
        Django version 3.2.19, using settings 'config.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.

        NOTE: Perubahan files

        new file:   .env.example
        modified:   .gitignore
        modified:   README.md
        modified:   config/settings.py


#### 24. Model - Membuat Category dan Sub_Category model

        # MODEL: Category
        class Category(models.Model):
                name = models.CharField(max_length=150)


        # MODEL: Sub_Category
        class Sub_Category(models.Model):
                name = models.CharField(max_length=150)
                category = models.ForeignKey(Category, on_delete=models.CASCADE)

        > python manage.py makemigrations
        ...
        Migrations for 'main':
          app\main\migrations\0001_initial.py
            - Create model Category
            - Create model Sub_Category

        > python manage.py migrate

        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, main, sessions
        Running migrations:
          Applying main.0001_initial... OK

        mysql> SHOW tables;
        +----------------------------------------+
        | Tables_in_django_e_shopper_multivendor |
        +----------------------------------------+
        | auth_group                             |
        | auth_group_permissions                 |
        | auth_permission                        |
        | auth_user                              |
        | auth_user_groups                       |
        | auth_user_user_permissions             |
        | django_admin_log                       |
        | django_content_type                    |
        | django_migrations                      |
        | django_session                         |
        | main_category                          |
        | main_sub_category                      |
        +----------------------------------------+
        12 rows in set (0.00 sec)

        mysql> DESC main_category;
        +-------+--------------+------+-----+---------+----------------+
        | Field | Type         | Null | Key | Default | Extra          |
        +-------+--------------+------+-----+---------+----------------+
        | id    | bigint(20)   | NO   | PRI | NULL    | auto_increment |
        | name  | varchar(150) | NO   |     | NULL    |                |
        +-------+--------------+------+-----+---------+----------------+
        2 rows in set (0.00 sec)

        mysql> DESC main_sub_category;
        +-------------+--------------+------+-----+---------+----------------+
        | Field       | Type         | Null | Key | Default | Extra          |
        +-------------+--------------+------+-----+---------+----------------+
        | id          | bigint(20)   | NO   | PRI | NULL    | auto_increment |
        | name        | varchar(150) | NO   |     | NULL    |                |
        | category_id | bigint(20)   | NO   | MUL | NULL    |                |
        +-------------+--------------+------+-----+---------+----------------+
        3 rows in set (0.00 sec)

        modified:   README.md
        new file:   app/main/migrations/0001_initial.py
        modified:   app/main/models.py


#### 25. Model - Register Category dan Sub_Category model pada main/admin.py

        modified:   README.md
        modified:   app/main/admin.py


#### 26. Model - Menambahkan meta class pada Category dan Sub_Category model

        modified:   README.md
        modified:   app/main/admin.py
        modified:   app/main/models.py


#### 27. Model - Meng-input category melalui admin

        modified:   README.md
