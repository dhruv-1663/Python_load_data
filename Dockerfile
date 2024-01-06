FROM python

COPY . /task1

WORKDIR /task1

RUN pip install -r requirements.txt

