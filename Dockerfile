FROM python:3.11

WORKDIR /task1

RUN apt update

RUN apt install vim -y

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./main .
