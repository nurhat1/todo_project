## After cloning the repository create a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

## Install dependencies
`pip install -r requirements.txt`

Next, you need to create a .env file for sensitive data.

## Run migrations and create a superuser
```
python manage.py migrate
python manage.py createsuperuser
```

## Commands to run the project and celery
```
python manage.py runserver
celery -A todo_project worker -l debug
```