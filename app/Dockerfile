FROM ubuntu:16.04
MAINTAINER Sotiris Karageorgopoulos <sotiriskarageorgopoulos@gmail.com>
RUN apt-get update &&\
    apt-get install -y python3 python3-pip &&\
    pip3 install flask pymongo &&\
    apt-get install -y locales &&\
    mkdir /app &&\
    mkdir -p /app/static &&\
    mkdir -p /app/templates &&\
    locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
WORKDIR /app
COPY movieflix.py /app/movieflix.py
ADD static /app/static
ADD templates /app/templates
EXPOSE 5000
ENTRYPOINT [ "python3","-u","movieflix.py" ]