#!/bin/bash
set -x;
# 1st option - Start the kafka server with zookeeper
# Start the zookeeper server in the background
# /bin/bash $KAFKA_HOME/bin/zookeeper-server-start.sh $KAFKA_HOME/config/zookeeper.properties &

# echo "advertised.listeners=PLAINTEXT://127.0.0.1:9092" >> $KAFKA_HOME/config/server.properties

# Start the kafka-server in the foreground
# /bin/bash $KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties

# 2nd option - Start the kafka server with KRaft - use the code below

export KAFKA_CLUSTER_ID="$($KAFKA_HOME/bin/kafka-storage.sh random-uuid)"

/bin/bash $KAFKA_HOME/bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c $KAFKA_HOME/config/kraft/server.properties

export CONTAINER_ID=$(hostname -I | sed 's/ //g')

echo "advertised.listeners=PLAINTEXT://$CONTAINER_ID:9092" >> $KAFKA_HOME/config/kraft/server.properties
# echo "advertised.listeners=PLAINTEXT://127.0.0.1:9092" >> $KAFKA_HOME/config/kraft/server.properties

/bin/bash $KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/kraft/server.properties

trap : TERM INT; sleep infinity & wait