FROM ubuntu:16.04
MAINTAINER Sotiris Karageorgopoulos <sotiriskarageorgopoulos@gmail.com>
RUN apt-get update &&\
    apt-get install -y python3 python3-pip &&\
    pip3 install flask pymongo &&\
    mkdir /app &&\
    mkdir -p /app/static &&\
    mkdir -p /app/templates
WORKDIR /app
COPY movieflix.py /app/movieflix.py
ADD static /app/static
ADD templates /app/templates
EXPOSE 5000
ENTRYPOINT [ "python3","-u","movieflix.py" ]