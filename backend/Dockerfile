# syntax=docker/dockerfile:1

FROM python:3.10

LABEL maintainer="Fernado Cruz"

ARG GROUPID
ARG USERID

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y gosu supervisor

WORKDIR /code

COPY requirements.txt /code/

RUN groupadd --force -g $GROUPID fly
RUN useradd -ms /bin/bash --no-user-group -g $GROUPID -u $USERID fly

COPY start-container /usr/local/bin/start-container
COPY wait-for-it.sh /
COPY entry_point.sh /
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN chmod +x /usr/local/bin/start-container

USER fly

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["start-container"]
