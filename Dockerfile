# pull official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /API

# set env variables
ENV ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependancies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
