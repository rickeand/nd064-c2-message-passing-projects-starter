from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LocationsMessage(_message.Message):
    __slots__ = ["person_id", "creation_time", "latitude", "longitude"]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    person_id: int
    creation_time: str
    latitude: str
    longitude: str
    def __init__(self, person_id: _Optional[int] = ..., creation_time: _Optional[str] = ..., latitude: _Optional[str] = ..., longitude: _Optional[str] = ...) -> None: ...
