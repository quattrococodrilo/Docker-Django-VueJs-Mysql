FROM node

COPY ./app/ /code

WORKDIR /code

COPY wait-for-it.sh /

COPY entry_point.sh /

RUN npm install