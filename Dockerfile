FROM python:3.9-slim

WORKDIR /task1

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./main/ /task1/

