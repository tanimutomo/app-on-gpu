FROM nvidia/cuda:10.2-runtime-ubuntu18.04

WORKDIR /app 
ADD requirements.txt /app

RUN apt update && \
    apt install -y python3-pip && \
    apt install -y libsm6 libxext6 libxrender-dev

RUN pip3 install -r requirements.txt

ADD . /app

CMD ["uwsgi", "app.ini"]