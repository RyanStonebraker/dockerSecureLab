FROM ubuntu:latest

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y python3 python3-pip

WORKDIR /app/src
COPY ./src /app/src

RUN pip3 install -r requirements.txt

CMD python3 /app/src/server.py