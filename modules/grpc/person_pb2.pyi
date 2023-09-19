from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PersonsMessage(_message.Message):
    __slots__ = ["id", "first_name", "last_name", "company_name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    first_name: str
    last_name: str
    company_name: str
    def __init__(self, id: _Optional[int] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., company_name: _Optional[str] = ...) -> None: ...
