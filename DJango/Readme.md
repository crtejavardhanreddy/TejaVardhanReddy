# <p style="text-align: center;">Django </p>

## Intro
Django is a framework for web-applications especially for developing backend using python.

- Before starting create vitual env and install Django using `pip install django`

- To start/create a new project   
`django-admin startproject <project_name>`

- create number of apps for each feature or service in the **root directory** where `manage.py` file exists.<br>
`python manage.py startapp <app_name>`
> After creating the app you will find the following.

    1) Admin --> database actions will be stored in `admin.py`.
    2) Urls --> endpoints are in `urls.py` mapped with app urls `<app_name>/urls.py`
    3) Views --> functions/methods(actual logic) that are routed from `urls.py` in `views.py`
        - Pass all the variables to front-end and read as only one object(json,dict) 
    4) Models --> Database connections

>To start the server `python manage.py runserver`

## Concepts

- URL routing
- Rendering templates
- Dynamically Data reading
- Word Counter (Read and Write the data)
<!-- - POST Use `_post` while deconding in the backend -->
- Models(Database connections based on our requirement)<br>
    `make migrations of your database models by adding your app into the settings.py file`<br>
    > 1) `python manage.py makemigrations`<br>
    > 2) `python manage.py migrate`
    > 3) `python .\manage.py createsuperuser`
    > 4) register your models in the admin `admin.site.register(model_name)`
- user register
- user login/logout
- dynamic url routing (manually enter the '/' in dynamic routing and in static ignore the '/')


## REST framework
- `pip install djangorestframework`
- Enter `rest_framework` in the settings.py file in Installed_apps section
- Before starting the server migrate everything to the database
- Protect your apis
- ViewSets and Serializers
- Default routers


## Steps to follow for API creation
1) Download rest framework (DRF) (apps)
2) Setup Models(database) (models)
3) Setup Serializers (models serializer)
4) Setup views (model viewset)
5) Setup Urls (urls for views)
6) Test APIs (test apis)



