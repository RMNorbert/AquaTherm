FROM python:3.11-alpine

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

WORKDIR /var/server
ADD . /var/server

CMD python web_app.py