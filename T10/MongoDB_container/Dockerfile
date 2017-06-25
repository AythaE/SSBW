FROM mvertes/alpine-mongo:latest
# Reference https://docs.docker.com/engine/reference/builder/#label
LABEL maintainer "AythaE <aythae@correo.ugr.es>"

RUN apk update && apk upgrade 

COPY mongodb /etc/conf.d/

WORKDIR /root/

ENTRYPOINT [ "/root/run.sh" ]
CMD [ "mongod" ]
