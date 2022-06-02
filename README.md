# Lab - Class 33

## Project:  Authentication & Production Server

### Author: Matt Rangel

### Links and Resources

- [Django](https://www.djangoproject.com)
- [Docker](https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html)
- Morning Lecture

### Setup

- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install django`
- `django-admin start project <project name>`
- `python manage.py migrate`
- `python manage.py runserver`
- `python manage.py startapp <app name>`
- `python manage.py makemigrations <app name>`
- `python manage.py migrate`
  - `python manage.py createsuperuser`
  - `UserName: <admin name>`
  - `password: <password>`
- `python manage.py runserver`

### Set up User

- `pip install djangorestframework`
- `pip freeze > requirements.txt`
- `docker compose run`
- `docker-compose up --build`
- `docker-compose run web python manage.py migrate`
- `docker-compose run web bash`

1. `create a super user`
2. access `/api/token/` then login in the admin with previously super user credentials
3. You will see the below(the token is time sensitive to 5 minutes, be aware)
  *1.* `refresh`: `token`(it's garbled, but it's the token)
  *2.* `access`: `token`(it's garbled, but it's the token)
4. Copy the `refresh` token and navigate to `/api/token/refresh`
5. Post the token to refresh field
6. Now you will have the `access` token, copy that and go to the thunder client.
7. Make a new request and enter `http://localhost:8000/api/v1/sounds`
8. Click on `Auth` and then `Bearer`
9. Then paste in the `access` token into the bearer token field.
10. This will tell you whether or not your token `Passed` or `Failed`
11. Toggle to `POST` a `1`, `2`, or a `3` after as so `http://localhost:8000/api/v1/sounds/1`

### Tests

No Unit Tests are required
