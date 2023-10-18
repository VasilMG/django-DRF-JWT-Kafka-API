# kafka_consumers/management/commands/second_consumer.py
from django.core.management.base import BaseCommand
from threading import Thread
from InterviewSystem.interview_app.consumers import status_consumer

class Command(BaseCommand):
    help = 'Start Kafka consumers as threads'

    def handle(self, *args, **options):
        thread = Thread(target=status_consumer)

        thread.start()
