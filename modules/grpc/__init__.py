import json
import logging
import grpc
import concurrent.futures as futures
import time
import location_pb2_grpc

from kafka import KafkaProducer

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("grpc")

KAFKA_SERVER = 'localhost:9092'
KAFKA_TOPIC = 'location'


class LocationService(location_pb2_grpc.LocationServiceServicer):

    def Create(self, request, context):
        data = json.dumps({
            'person_id': request.person_id,
            'latitude': request.latitude,
            'longitude': request.longitude
        })
        kafka_config = {
            'bootstrap_servers': KAFKA_SERVER
        }
        kafka = KafkaProducer(**kafka_config)
        kafka.send(
            topic=KAFKA_TOPIC,
            value=data
        )
        kafka.flush()
        return request

def start_server():
    # Initialize gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    location_pb2_grpc.add_LocationServiceServicer_to_server(LocationService(), server)

    logging.info("Location server starting on port 5005...")
    server.add_insecure_port("[::]:5005")
    server.start()
    # Keep thread alive
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    logging.basicConfig()
    start_server()