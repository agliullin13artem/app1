FROM python:3.11.8


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app_dock

COPY requirements.txt /app_dock/


RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

COPY . /app_dock/


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]