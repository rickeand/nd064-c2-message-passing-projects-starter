import grpc
import location_pb2
import location_pb2_grpc

channel = grpc.insecure_channel("localhost:5005")
location_stub = location_pb2_grpc.LocationServiceStub(channel)

# test location message
locations = location_pb2.LocationsMessage(
    person_id=1,
    creation_time='2023-01-01T10:10:10',
    latitude='123456789',
    longitude='234'
)

response = location_stub.Create(locations)
