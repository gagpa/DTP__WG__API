FROM python:3.9.5-slim-buster

RUN mkdir -p /app/
WORKDIR /app/
COPY requirements.txt requirements.txt
EXPOSE 8000
RUN apt update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
