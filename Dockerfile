FROM python:3.7.5
ENV LANG en_US.utf8
WORKDIR /app
ADD requirements.txt /app
RUN apt-get update
RUN pip install -r requirements.txt
