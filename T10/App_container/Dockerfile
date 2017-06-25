FROM python:3.4-alpine
# Reference https://docs.docker.com/engine/reference/builder/#label
LABEL maintainer "AythaE <aythae@correo.ugr.es>"

RUN apk update && apk upgrade \
    && apk add gcc linux-headers musl-dev supervisor python3-dev freetype-dev libjpeg-turbo-dev lcms2-dev openjpeg-dev tiff-dev libwebp-dev libxml2-dev libxslt-dev zlib-dev\
    && mkdir -p /code/app

COPY requirements.txt /code/

WORKDIR /code/

RUN pip install -r requirements.txt \
    && pip install uwsgi \
    && apk del gcc linux-headers musl-dev

COPY app/ /code/app

COPY app.ini /code/uwsgi/
COPY supervisord.conf /etc/

EXPOSE 8000

CMD ["supervisord", "-n"]
