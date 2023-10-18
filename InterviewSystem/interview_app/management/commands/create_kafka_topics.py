import json
import os

from django.core.management import BaseCommand
from kafka.admin import KafkaAdminClient, NewTopic

from kafka import KafkaConsumer
kafka_host = os.getenv('KAFKA_HOST', 'localhost')

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Define Kafka broker(s) and topic name
        broker_list = f"{kafka_host}:9092"  # Replace with your Kafka broker(s)
        topic_name1 = "Candidates"
        topic_name2 = "InterviewChange"
        print(broker_list)

        # Create an admin client
        admin_client = KafkaAdminClient(bootstrap_servers=broker_list)

        topic_config = {
            "cleanup.policy": "delete",  # Replace with your desired topic configuration
        }

        # Create a NewTopic object with the topic name and configuration
        new_topic1 = NewTopic(
            name=topic_name1,
            num_partitions=1,  # Specify the number of partitions
            replication_factor=1,  # Specify the replication factor

        )

        new_topic2 = NewTopic(
            name=topic_name2,
            num_partitions=1,  # Specify the number of partitions
            replication_factor=1,  # Specify the replication factor
        )

        admin_client.create_topics([new_topic1, new_topic2])
        admin_client.close()


