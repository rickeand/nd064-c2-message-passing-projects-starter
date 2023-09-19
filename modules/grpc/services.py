import logging
import json

from app import db
from app.udaconnect.models import Connection, Location, Person
from app.udaconnect.schemas import ConnectionSchema, LocationSchema, PersonSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text

from kafka.producer import KafkaProducer
from kafka.consumer import KafkaConsumer

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("grpc")


class KafkaService:

    TOPIC_NAME = 'locations'
    KAFKA_SERVER = 'localhost:9092'

    @staticmethod
    def sendLocation(location_data):
        KAFKA_PRODUCER = KafkaProducer(bootstrap_servers=KafkaService.KAFKA_SERVER)
        kafka_data = json.dumps(location_data).encode()
        KAFKA_PRODUCER.send(KafkaService.TOPIC_NAME, kafka_data)
        KAFKA_PRODUCER.flush()
        return location_data
