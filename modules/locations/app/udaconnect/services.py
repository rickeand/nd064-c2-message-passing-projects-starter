import json
import logging

from app import db
from app.udaconnect.models import Location
from geoalchemy2.functions import ST_AsText, ST_Point

from kafka import KafkaConsumer

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("kafka-consumer")

KAFKA_SERVER = 'kafka-service:9092'
KAFKA_TOPIC = 'location'


class KafkaConsumerService:

    @staticmethod
    def consumeLocation():
        kafka_config = {
            'bootstrap_servers': KAFKA_SERVER
        }
        locations = KafkaConsumer(KAFKA_TOPIC, **kafka_config)
        for location in locations:
            location = json.loads(location.value.decode("utf-8"))
            new_location = Location()
            new_location.person_id = location["person_id"]
            new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
            db.session.add(new_location)
            db.session.commit()


class LocationService:
    @staticmethod
    def retrieve(location_id) -> Location:
        location, coord_text = (
            db.session.query(Location, Location.coordinate.ST_AsText())
            .filter(Location.id == location_id)
            .one()
        )

        # Rely on database to return text form of point to reduce overhead of conversion in app code
        location.wkt_shape = coord_text
        return location