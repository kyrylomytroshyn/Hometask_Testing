# Dockerfile
# Pull base image

FROM python:3.9
# Set environment variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.8.0/wait /wait
RUN chmod +x /wait
# Set work directory

WORKDIR /code
# Install dependencies

COPY ./requirements.txt  /code/
RUN pip install -r requirements.txt
