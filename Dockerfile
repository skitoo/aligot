FROM ubuntu:latest
MAINTAINER Alexis Couronne <http://www.skitoo.net>


RUN apt-get -y update
RUN apt-get install -y python python-pip libpq-dev python-dev

ADD . /aligot
WORKDIR /aligot

RUN pip install -r requirements.txt
RUN pip install pytest

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE aligot.settings
