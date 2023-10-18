import json
import os

from kafka import KafkaConsumer
from InterviewSystem.interview_app.models import SentEmail
kafka_host = os.getenv('KAFKA_HOST', 'localhost')

def candidate_consumer():
    topic1 = 'Candidates'
    consumer = KafkaConsumer(topic1,
                             bootstrap_servers=f'{kafka_host}:9092',
                             auto_offset_reset='earliest',  # Set to 'earliest' to read all messages from the beginning
                             enable_auto_commit=True,
                             auto_commit_interval_ms=1000,
                             # consumer_timeout_ms=1000,
                             value_deserializer=lambda m: json.loads(m.decode('utf-8'))
                             )

    for message in consumer:
        # Logic to send an email to the Dev department with the new candidate

        email = SentEmail.objects.create(
            sent_data= f'Candidate Consumer - Topic: {message.topic}. Message:{message.value}'
        )
        email.save()
        print(f'Candidate Consumer - Topic: {message.topic}. Message:{message.value}')

def status_consumer():
    topic2 = 'InterviewChange'
    consumer = KafkaConsumer(topic2,
                             bootstrap_servers=f'{kafka_host}:9092',
                             auto_offset_reset='earliest',  # Set to 'earliest' to read all messages from the beginning
                             enable_auto_commit=True,
                             auto_commit_interval_ms=1000,
                             # consumer_timeout_ms=1000,
                             value_deserializer=lambda m: json.loads(m.decode('utf-8'))
                             )

    for message in consumer:
        # Logic to send an email to HR department with the new feedback
        email = SentEmail.objects.create(
            sent_data=f'Status Consumer - Topic: {message.topic}. Message:{message.value}'
        )
        email.save()
        print(f'Status Consumer - Topic: {message.topic}. Message:{message.value}')
