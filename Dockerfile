FROM ubuntu:24.04

RUN apt update -y &&\
    apt-get install x11-apps -y;

RUN apt -y install colmap imagemagick  python3-pip