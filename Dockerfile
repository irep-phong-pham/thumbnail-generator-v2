# FROM 164108310211.dkr.ecr.us-east-1.amazonaws.com/dockerhub_tiangolo_uwsgi-nginx-flask:python3.10
FROM tiangolo/uwsgi-nginx-flask:python3.10

RUN apt-get update \
    && apt-get clean

WORKDIR /app

ENV PYTHONPATH /app

RUN pip install pipenv && pipenv --version

COPY . /app

RUN pipenv lock

RUN pipenv install --system --deploy

RUN chmod +x prestart.sh tests/test.sh

EXPOSE 5000