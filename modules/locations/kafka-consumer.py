import os
import logging

from app import create_app
from app.udaconnect.services import KafkaConsumerService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("kafka-consumer")

app = create_app(os.getenv("FLASK_ENV") or "test")
with app.app_context():
    logger.info("started kafka consumer")
    KafkaConsumerService.consumeLocation()
