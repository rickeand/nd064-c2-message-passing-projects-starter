import grpc
import location_pb2
import location_pb2_grpc
import person_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payloads...")

channel = grpc.insecure_channel("localhost:5005")
location_stub = location_pb2_grpc.LocationServiceStub(channel)
#person_stub = person_pb2_grpc.PersonServiceStub(channel)

# Update this with desired payload
locations = location_pb2.LocationsMessage(
    person_id=1,
    creation_time='2023-01-01T10:10:10',
    latitude='123456789',
    longitude='234'
)

"""persons = person_pb2.PersonsMessage(
    id = 1,
    first_name = 'Dung',
    last_name = 'Truong',
    company_name = 'FPT'
)"""


response = location_stub.Create(locations)
#response = person_stub.Create(persons)