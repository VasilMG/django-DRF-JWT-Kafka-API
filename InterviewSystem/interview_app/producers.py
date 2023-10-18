import json
import os

from kafka import KafkaProducer
kafka_host = os.getenv('KAFKA_HOST', 'localhost')



candidate_producer = KafkaProducer(
                bootstrap_servers=f'{kafka_host}:9092',
                value_serializer=lambda m: json.dumps(m).encode('utf-8')
            )

status_producer = KafkaProducer(
                bootstrap_servers=f'{kafka_host}:9092',
                value_serializer=lambda m: json.dumps(m).encode('utf-8')
            )

