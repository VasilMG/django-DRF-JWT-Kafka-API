# kafka_consumers/management/commands/first_consumer.py
from django.core.management.base import BaseCommand
from threading import Thread
from InterviewSystem.interview_app.consumers import candidate_consumer, status_consumer

class Command(BaseCommand):
    help = 'Start Kafka consumers as threads'

    def handle(self, *args, **options):
        # Create and start threads for each consumer
        thread1 = Thread(target=candidate_consumer)


        thread1.start()
