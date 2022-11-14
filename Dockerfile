FROM python:3.10
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
RUN python manage.py migrate

EXPOSE 8000
CMD ["python","manage.py","runserver"]