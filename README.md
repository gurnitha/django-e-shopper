# MEMBUAT APLIKASI ECOMMERCE E-SHOPPER MENGGUNAKAN DJANGO V3.2

[Submber:](https://www.youtube.com/@CodingEx)


#### [1. Membuat virtual environment](https://github.com/gurnitha/django-e-shopper/commit/dc67501a10d6261e4a37db28876e143c72e031c4)

        new file:   .gitignore
        new file:   README.md

        > python -m venv venv3932


#### [2. Menginstall django v3.2](https://github.com/gurnitha/django-e-shopper/commit/2e356052889fb329c170374defad4e3b453ba327)

        new file:   .gitignore
        new file:   README.md

        > venv3932\Scripts\activate
        > pip install django==3.2.*
        ...
         Downloading Django-3.2.19-py3-none-any.whl (7.9 MB)


#### [3. Meng-upgrade pip](https://github.com/gurnitha/django-e-shopper/commit/907d553fcb177854d2ff42941245c4e6a330eafa)

        new file:   .gitignore
        new file:   README.md

        > python.exe -m pip install --upgrade pip
        ...
        Successfully installed pip-23.1.2


#### [4. Memeriksa hasil instalasi](https://github.com/gurnitha/django-e-shopper/commit/2ec83b8cdf66c4eae7b2cfa7c5abf2c5e5618374)

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


#### [5. Membuat django proyek dengan nama'config'](https://github.com/gurnitha/django-e-shopper/commit/ee5fafeb12130dd5cde60d402c221673fe05d66a)

        > django-admin startproject config .
        ...
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### [6. Membuat django app dengan nama 'main'](https://github.com/gurnitha/django-e-shopper/commit/76ebaf67109ffda3b65bb94945dd1ffa02b55757)

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


#### [7. Register main app pada proyek config](https://github.com/gurnitha/django-e-shopper/commit/1f309f625d8d7d0601f42c9fee364dacd97541aa)

        modified:   .gitignore
        modified:   README.md
        modified:   app/main/apps.py
        modified:   config/settings.py


#### [8. Menjalankan django lokal server dan menampilkan django pada web browser](https://github.com/gurnitha/django-e-shopper/commit/2aaff75c76c3e61e6b1431f0c719a4098f30c053)

        > python manage.py runserver
        > http://127.0.0.1:8000/


#### [9. Membuat halo world](https://github.com/gurnitha/django-e-shopper/commit/880d598770c6efccaf282e9f9466728c31573773)

        modified:   README.md
        new file:   app/main/urls.py
        modified:   app/main/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/app/main/index.html

        : 'DIRS': ['templates'],


#### [10. Mengisi html template pada home page](https://github.com/gurnitha/django-e-shopper/commit/743cd7b51c0e8f298e2d13bac1e89adc9b906e53)

        modified:   README.md
        modified:   templates/app/main/index.html


#### [11. Mengisi assets (css,js,images,fonts)](https://github.com/gurnitha/django-e-shopper/commit/52a5c9f2c2e6f25a5e972d812d372171ca0531e7)

        modified:   .gitignore
        modified:   README.md

        : static


#### [12. Membuat path untuk static_root dan staticfiles_dir](https://github.com/gurnitha/django-e-shopper/commit/200d75bd79586e807a56f423ec8774e6a898bd2f)

        modified:   README.md
        modified:   config/settings.py

        : STATIC_URL  = '/static/'
        : STATIC_ROOT = '/static/'
        : STATICFILES_DIRS = [
        	os.path.join(BASE_DIR, 'static')
          ]


#### [13. Loding static files]()

        modified:   README.md
        modified:   config/settings.py

        : STATIC_URL  = '/static/'
        : STATIC_ROOT = '/static/'
        : STATICFILES_DIRS = [
        	os.path.join(BASE_DIR, 'static')
          ]


#### [14. Membuat base.html file](https://github.com/gurnitha/django-e-shopper/commit/dbda67ddb82fd4dee0b628f3c8491107d5b5f4df)

        modified:   README.md
        modified:   templates/app/main/index.html
        new file:   templates/base.html


#### [15. Memindahkan html template dari index.html ke base.html](https://github.com/gurnitha/django-e-shopper/commit/3e47cf74544e160da0f20a0631ed8feee88a74db)

        modified:   README.md
        modified:   templates/app/main/index.html
        new file:   templates/base.html


#### [16. Meng-extends base.html ke index.html](https://github.com/gurnitha/django-e-shopper/commit/8cb86bdb0b6ec15b5736511fc2a57636940f09ed)

        modified:   README.md
        modified:   templates/app/main/index.html


#### [17. Men-sagmentasi base.html template dan template inheritance](https://github.com/gurnitha/django-e-shopper/commit/603d1a26d5be97894f5acd9cb0e27dc48fbde79e)

        modified:   README.md
        new file:   templates/app/main/components/content.html
        new file:   templates/app/main/components/slider.html
        modified:   templates/app/main/index.html
        modified:   templates/base.html
        new file:   templates/partials/_footer.html
        new file:   templates/partials/_header.html
        new file:   templates/partials/_scripts.html


#### [18. Men-sagmentasi content index.html](https://github.com/gurnitha/django-e-shopper/commit/92c4e71dd64938632d668aa1eb13cd95ad12ff45)

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


#### [19. Membuat page title](https://github.com/gurnitha/django-e-shopper/commit/534e7a2a4c24889f2c6ba56b49966abea4708d8e)

        modified:   README.md
        modified:   templates/app/main/index.html
        modified:   templates/base.html


#### [20. Database - Create MySQL database](https://github.com/gurnitha/django-e-shopper/commit/93538aecae7b37970879b0bb8385451a0f39e45b)

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


#### 28. Model - Meng-input sub_category melalui admin

        modified:   README.md


#### 29. READ - Load and display categories

        modified:   README.md
        modified:   app/main/views.py
        modified:   templates/app/main/components/category_products.html

        NOTE:

        1. Sukses display categories
        2. Link tidak bekerja

        NEXT:

        #### 30. READ - Load and display sub_categories


#### 30. READ - Load and display sub_categories

        modified:   README.md
        modified:   templates/app/main/components/category_products.html

        NOTE:

        1. Sukses display categories
        2. Sukses display sub_category

        NEXT:

        #### 31. Membuat link dropdown bekerja


#### 31. READ - Membuat link dropdown bekerja

        modified:   README.md
        modified:   templates/app/main/components/category_products.html

        NOTE:

        1. Sukses display categories
        2. Sukses display sub_category
        3. Klik dropdown bekerja

        NEXT:

        CRUD - Create Products model


#### 33. CREATE - Membuat Product model

        modified:   README.md
        modified:   app/main/models.py
        
        NEXT:

        CREATE - Add 1-M relationship Category dan Product models



#### 34.  CREATE - Add 1-M relationship Category, Sub_Category dengan Product models

        0. > pip install pillow
        
        1. Membuat Product model dan relationship dengan Category dan Sub_Category models

        # MODEL: Product
        class Product(models.Model):
                category = models.ForeignKey(Category, on_delete=models.CASCADE)
                sub_category = models.ForeignKey(Sub_Category,         on_delete=models.CASCADE)
                name = models.CharField(max_length=150)
                image = models.ImageField(upload_to='uploads/images/products/')
                price = models.IntegerField()
                date = models.DateField(auto_now_add=True)

                class Meta:
                        verbose_name = 'Product'
                        verbose_name_plural = 'Products'

                def __str__(self):
                        return self.name

        2. > python manage.py makemigrations

        Migrations for 'main':
          app\main\migrations\0002_auto_20230512_1343.py
            - Change Meta options on category
            - Change Meta options on sub_category
            - Create model Product

        3. > python manage.py migrate

        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, main, sessions
        Running migrations:
          Applying main.0002_auto_20230512_1343... OK

        modified:   README.md
        new file:   app/main/migrations/0002_auto_20230512_1343.py
        modified:   app/main/models.py
        
        NEXT:

        Register Product model pada main/admin.py


#### 35. Register Product model pada main/admin.py

        modified:   README.md
        modified:   app/main/admin.py


#### 36. Add, load and display products as feature products

        modified:   README.md
        modified:   app/main/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        ...
        new file:   uploads/images/products/product5.jpg
        new file:   uploads/images/products/product6.jpg

        NEXT:

        Filter product by category


#### 37. Dispaly products by Category and Sub_Category

        modified:   README.md
        modified:   app/main/views.py
        new file:   media/uploads/images/products/girl1.jpg
        modified:   templates/app/main/components/category_products.html


#### 38. USERAUTH - Membuat userauth app

        modified:   README.md
        new file:   app/userauth/__init__.py
        new file:   app/userauth/admin.py
        new file:   app/userauth/apps.py
        new file:   app/userauth/migrations/__init__.py
        new file:   app/userauth/models.py
        new file:   app/userauth/tests.py
        new file:   app/userauth/views.py
        modified:   config/settings.py


#### 39. USERAUTH - Membuat UserCreationForm model

        modified:   README.md
        modified:   app/userauth/models.py


#### 40. USERAUTH - Membuat signup form: part 1

        modified:   README.md
        new file:   app/userauth/urls.py
        modified:   app/userauth/views.py
        modified:   config/urls.py
        new file:   templates/app/userauth/registration/signup.html


#### 41. USERAUTH - Membuat logik pada signup_page

        modified:   README.md
        modified:   app/userauth/views.py


#### 42. USERAUTH - Membuat signup form: part 2 - membuat form field untuk signup

        modified:   README.md
        modified:   templates/app/userauth/registration/signup.html

        NOTE:

        User baru sukses signup


#### 43. USERAUTH - Show or hide login and logout menu

        modified:   README.md
        modified:   templates/partials/_header.html


#### 43. USERAUTH - Login

        modified:   README.md
        modified:   app/userauth/models.py
        modified:   app/userauth/urls.py
        modified:   app/userauth/views.py
        modified:   config/urls.py
        modified:   templates/app/userauth/registration/signup.html
        modified:   templates/partials/_header.html
        new file:   templates/registration/login.html

        NOTE:

        1. Attribute form login come from here config/urls.py:
         path('accounts/', include('django.contrib.auth.urls')),

        2. When logged in, automatically redirect to: accounts/profile

        3. But it still needs: views method, and urls


#### 44. USERAUTH - Redirect to home page after logging in

        modified:   README.md
        modified:   config/settings.py
        modified:   templates/partials/_header.html


#### 45. USERAUTH - Mendefinisikan ulang path signup dan login

        new file:   app/userauth/_urls.py
        deleted:    app/userauth/urls.py
        modified:   app/userauth/views.py
        modified:   config/urls.py
        modified:   templates/partials/_header.html
        modified:   templates/registration/login.html
        renamed:    templates/app/userauth/registration/signup.html -> templates/registration/signup.html

        NOTE:

        Links yang dibetulkan:

        1. Login pada navbar
        2. Login pada signup form
        3. Signup pada login form

        Tested :)


#### 46. USERAUTH - Logout 

        modified:   README.md
        modified:   templates/partials/_header.html


#### 47. USERAUTH - Password reset 

        modified:   README.md
        modified:   templates/registration/login.html
        new file:   templates/registration/password_reset_complete.html
        new file:   templates/registration/password_reset_confirm.html
        new file:   templates/registration/password_reset_done.html
        new file:   templates/registration/password_reset_form.html

        NEXT:

        Setup smtp


#### 48. USERAUTH - Setup smtp server 

        modified:   config/settings.py

        NOTE:

        Did not work (Saya belum faham)


#### 49. SHOPPING CART - Setup shopping cart

        > pip install django-shopping-cart

        modified:   README.md
        modified:   app/main/views.py
        modified:   config/settings.py
        modified:   config/urls.py

        Source: https://codeingex.blogspot.com/2021/08/python-django-in-create-add-to-cart.html


#### 50. SHOPPING CART - Membuat laman cart_detail

        modified:   README.md
        modified:   app/main/views.py
        new file:   templates/app/cart/cart_detail.html
        modified:   templates/app/main/components/features_items.html


#### 51. SHOPPING CART - Add functionalities to cart_detail

        modified:   README.md
        modified:   app/main/views.py
        modified:   templates/app/cart/cart_detail.html
        modified:   templates/partials/_header.html

        NOTE:

        1. Jika user yg tdk login mencoba 'add to cart', maka
           terjadi error: PAGE NOT FOUND denga url spt dibawah ini: 
           http://127.0.0.1:8000/users/login?next=/cart/add/1/

        2. Jika user ingin berbelanja, maka di harus login
           telebih dahulu kalau sdh memiliki akun.

        3. Jika user belum memiliki akun dan ingin berbelanja,
           maka dia harus signup dulu.


#### 52. SHOPPING CART - Melindungi cart dari un-logged in user

        modified:   README.md
        modified:   app/main/views.py


#### 53. CONTACT - Create app 'app/contact'

        modified:   README.md
        new file:   app/contact/__init__.py
        new file:   app/contact/admin.py
        new file:   app/contact/apps.py
        new file:   app/contact/migrations/__init__.py
        new file:   app/contact/models.py
        new file:   app/contact/tests.py
        new file:   app/contact/views.py
        modified:   config/settings.py


#### 54. CONTACT - Create laman contact

        new file:   app/contact/urls.py
        modified:   app/contact/views.py
        modified:   config/urls.py
        new file:   templates/app/contact/contact.html


#### 55. CONTACT - Add html template pada laman contact

        new file:   templates/app/contact/contact.html


#### 56. CONTACT - Add Google Map pada laman contact

        new file:   templates/app/contact/contact.html


#### 57. CONTACT - Add address

        new file:   templates/app/contact/contact.html


#### 58. CONTACT - Membuat Contact model

        Aktifitas:

        1. Membuat Contact model

        # MODEL: Contact
        class Contact(models.Model):
                name = models.CharField(max_length=150)
                email = models.EmailField(max_length=150)
                subject = models.CharField(max_length=150)
                message = models.TextField()

                class Meta:
                        verbose_name = 'Contact'
                        verbose_name_plural = 'Contacts'

                def __str__(self):
                        return self.name

        2. Menjalan perintah migrasi

        > (venv3932) hp@ING:~$ python manage.py makemigrations
        Migrations for 'contact':
          app\contact\migrations\0001_initial.py
            - Create model Contact

        > (venv3932) hp@ING:~$ python manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contact, contenttypes, main, sessions
        Running migrations:
          Applying contact.0001_initial... OK

        3. Memeriksa hasil migrasi

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
        | contact_contact                        |
        | django_admin_log                       |
        | django_content_type                    |
        | django_migrations                      |
        | django_session                         |
        | main_category                          |
        | main_product                           |
        | main_sub_category                      |
        +----------------------------------------+
        14 rows in set (0.00 sec)

        mysql> DESC contact_contact;
        +---------+--------------+------+-----+---------+----------------+
        | Field   | Type         | Null | Key | Default | Extra          |
        +---------+--------------+------+-----+---------+----------------+
        | id      | bigint(20)   | NO   | PRI | NULL    | auto_increment |
        | name    | varchar(150) | NO   |     | NULL    |                |
        | email   | varchar(150) | NO   |     | NULL    |                |
        | subject | varchar(150) | NO   |     | NULL    |                |
        | message | longtext     | NO   |     | NULL    |                |
        +---------+--------------+------+-----+---------+----------------+
        5 rows in set (0.00 sec)

        4. Register Contact model to contact/admin.py

        # app/contact/admin.py

        # Import django modules & third parties
        from django.contrib import admin

        # Import from locals
        from app.contact.models import Contact

        # Register your models here.

        admin.site.register(Contact)

        5. Perubahan files

        modified:   README.md
        modified:   app/contact/admin.py
        new file:   app/contact/migrations/0001_initial.py
        modified:   app/contact/models.py


#### 59. CONTACT - Membuat logik pada Contact method dan testing

        Aktifitas:

        1. Membuat logik

        # Import from locals
        from app.contact import models
        # Create your views here.

        def contact_page(request):
                
                if request.method == 'POST':
                        contact = models.Contact(
                                name = request.POST.get('name'),
                                email = request.POST.get('email'),
                                subject = request.POST.get('subject'),
                                message = request.POST.get('message'),
                        )

                        contact.save()

                return render(request, 'app/contact/contact.html')

        2. Menambahkan csrf token pada form

        {% csrf_token %}

        3. Testing: Mengirim pesan

        4. Hasil testing :)

        5. Perubhan files

        modified:   README.md
        modified:   app/contact/views.py
        modified:   templates/app/contact/contact.html


#### 60. CONTACT - Add link contact dengan menu navigasi

        Aktifitas:

        1. Membuat link

        modified:   README.md
        modified:   templates/partials/_footer.html
        modified:   templates/partials/_header.html

        2. Testing

        3. Hasil :)


#### 61. ORDER - Membuat app 'app/order'

        Aktifitas:

        1. Membuat dir baru app/order
        > mkdir app\order

        2. Membuat app order
        >  django-admin startapp order app\order

        3. Modifikasi file apps.py
        dari : name = 'order'
        menjadi: name = 'app.order'

        4. Meregistrasi app order pada config/settings.py
        'app.order.apps.OrderConfig',

        5. Perubahan files

        modified:   README.md
        new file:   app/order/__init__.py
        new file:   app/order/admin.py
        new file:   app/order/apps.py
        new file:   app/order/migrations/__init__.py
        new file:   app/order/models.py
        new file:   app/order/tests.py
        new file:   app/order/views.py
        modified:   config/settings.py

        6. Testing dan berhasil :)


#### 62. ORDER - Membuat Order model

        Aktifitas:

        1. Membuat Order model

        from django.db import models
        from django.contrib.auth.models import User 
        import datetime 

        # Import from locals
        from app.main.models import Product  

        # Create your models here.

        # MODEL: Order
        class Order(models.Model):
                product = models.ForeignKey(Product, on_delete=models.CASCADE)
                image = models.ImageField(upload_to='uploads/order/images/')
                user = models.ForeignKey(User, on_delete=models.CASCADE)
                quantity = models.CharField(max_length=5)
                price = models.IntegerField()
                address = models.TextField()
                phone = models.CharField(max_length=15)
                pincode = models.CharField(max_length=10)
                date = models.DateField(default=datetime.datetime.today)

                class Meta:
                        verbose_name = 'Order'
                        verbose_name_plural = 'Orders'

                def __str__(self):
                        return self.product

        2. Menjalankan perintah migrasi

        (venv3932) hp@ING:~$ python manage.py makemigrations
        Migrations for 'order':
          app\order\migrations\0001_initial.py
            - Create model Order

        (venv3932) hp@ING:~$ python manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contact, contenttypes, main, order, sessions
        Running migrations:
          Applying order.0001_initial... OK

        3. Memeriksa hasil migrasi

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
        | contact_contact                        |
        | django_admin_log                       |
        | django_content_type                    |
        | django_migrations                      |
        | django_session                         |
        | main_category                          |
        | main_product                           |
        | main_sub_category                      |
        | order_order                            |
        +----------------------------------------+
        15 rows in set (0.00 sec)

        mysql> DESC order_order;
        +------------+--------------+------+-----+---------+----------------+
        | Field      | Type         | Null | Key | Default | Extra          |
        +------------+--------------+------+-----+---------+----------------+
        | id         | bigint(20)   | NO   | PRI | NULL    | auto_increment |
        | image      | varchar(100) | NO   |     | NULL    |                |
        | quantity   | varchar(5)   | NO   |     | NULL    |                |
        | price      | int(11)      | NO   |     | NULL    |                |
        | address    | longtext     | NO   |     | NULL    |                |
        | phone      | varchar(15)  | NO   |     | NULL    |                |
        | pincode    | varchar(10)  | NO   |     | NULL    |                |
        | date       | date         | NO   |     | NULL    |                |
        | product_id | bigint(20)   | NO   | MUL | NULL    |                |
        | user_id    | int(11)      | NO   | MUL | NULL    |                |
        +------------+--------------+------+-----+---------+----------------+
        10 rows in set (0.00 sec)

        4. Register Order model pada order/admin.py

        # app/order/admin.py

        # Import django modules & third parties
        from django.contrib import admin

        # Import from locals
        from app.order.models import Order

        # Register your models here.

        admin.site.register(Order)

        5. Testing dan berhasil :)

        6. Perubahan files

        modified:   README.md
        new file:   app/order/migrations/0001_initial.py
        modified:   app/order/models.py


#### 62. ORDER - Fixing issue

        Aktifitas:

        1. Jenis issue

        TypeError at /admin/order/order/add/
        __str__ returned non-string (type Product)

        2. Fixing issue:

        BEFORE pada Order model:

        def __str__(self):
                        return self.product 


        AFTER pada Order model:

        def __str__(self):
                        return self.product.name

        3. Testing: add order dari admin dashboard

        4. Hasil: berhasil :)

        5. Perubahan files

        modified:   README.md
        modified:   app/order/models.py
        new file:   media/uploads/order/images/product6.jpg
        new file:   media/uploads/order/images/product6_L9Du4Ns.jpg


#### HOUSE KEPPING - Modifikasi README.md file