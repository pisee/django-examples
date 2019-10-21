# Django-examples

## installation
1. Create Virtual Environment
    ```
    $ pyton -m venv .venv
    ```
1. Virtual Environment activate
    - window
        ```
        $ [PATH_TO_.venv]/Scripts/activate.bat
        ```
    - mac os
        ```
        $ source [PATH_TO_.venv]/bin/activate
        ```
1. install python modules
    ```
    $ npm install -r requirements.txt
    ```
1. Django migrations
    ```
    python manage.py migrate
    ```
1. Django create super user
    ```
    python manage.py createsuperuser
    ```
1. Run Django web application
    ```
    $ python manage.py runserver
    ```
1. create contents http://localhost:8000/admin
1. polls app in http://localhost:8000/polls
1. check ```/api/polls```, ```/rest/polls``` for json comunication