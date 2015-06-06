FROM ubuntu:latest
MAINTAINER Alexis Couronne <http://www.skitoo.net>


RUN apt-get -y update
RUN apt-get install -y python python-pip nodejs npm
RUN apt-get install -y libpq-dev python-dev
RUN apt-get install -y nodejs-legacy

ADD . /aligot
WORKDIR /aligot

RUN pip install -r requirements.txt
RUN pip install pytest
RUN npm install

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE aligot.settings
