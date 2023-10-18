FROM python:3.10

ARG KAFKA_HOST

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV KAFKA_HOST=$KAFKA_HOST

WORKDIR /APP

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD exec /bin/bash ./start_api.sh
