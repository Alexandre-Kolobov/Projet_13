# pull the official base image
FROM python:3.10-alpine3.18

# set work directory
WORKDIR /usr/src/app

# set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1 - Forbid to create .pyc files (optimisation for container build)
# ENV PYTHONUNBUFFERED 1 - Send output logs to the termional without buffer
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app

CMD python manage.py runserver 0.0.0.0:$PORT