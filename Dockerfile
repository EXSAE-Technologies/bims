FROM python:3.10
WORKDIR /app
COPY . .

RUN export DJANGO_SUPERUSER_EMAIL=admin@test.com
RUN export DJANGO_SUPERUSER_PASSWORD=admin

RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py createsuperuser --username admin --email admin@test.com --no-input

EXPOSE 8000
CMD ["python","manage.py","runserver"]