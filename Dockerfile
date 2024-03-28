FROM python:3.12-alpine:3.18
ENV PYTHONUNBUFFERED 1
RUN mkdir /akowe
WORKDIR /akowe
ADD . /akowe/
RUN pip install -r requirements.txt