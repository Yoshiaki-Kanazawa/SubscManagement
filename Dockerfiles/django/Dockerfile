FROM python:3
ENV LANG en_US.utf8
ADD requirements.txt /
RUN apt-get update \
    && pip install -r requirements.txt
COPY ./app /app
WORKDIR /app