FROM python:3.5

MAINTAINER ebar0n

RUN pip install --upgrade pip setuptools
COPY ./requirements/base.pip /requirements/base.pip
COPY ./requirements/development.pip /requirements/development.pip
RUN pip install -r /requirements/development.pip 
