FROM debian:stable-slim

EXPOSE 9092


ENV KAFKA_VERSION=3.5.0
ENV KAFKA_SCALA_VERSION=2.13
ENV KAFKA_HOME="./kafka"

WORKDIR /server-kafka

RUN apt-get update && apt-get install -y \
    default-jre \
    wget sudo\
    && rm -rf /var/lib/apt/lists/*

# Download and extract Kafka
RUN wget -q "https://dlcdn.apache.org/kafka/${KAFKA_VERSION}/kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}.tgz" -O /tmp/kafka.tgz \
    && mkdir -p ${KAFKA_HOME} \
    && tar -xzf /tmp/kafka.tgz --strip-components=1 -C ${KAFKA_HOME} \
    && rm /tmp/kafka.tgz 

COPY ./docker-init-kafka-server.sh .

# RUN sed -i 's/\r$//' ./docker-init-kafka-server.sh

CMD exec /bin/bash ./docker-init-kafka-server.sh





