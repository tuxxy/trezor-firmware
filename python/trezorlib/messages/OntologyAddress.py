# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class OntologyAddress(p.MessageType):
    MESSAGE_WIRE_TYPE = 351

    def __init__(
        self,
        address: str = None,
    ) -> None:
        self.address = address

    @classmethod
    def get_fields(cls):
        return {
            1: ('address', p.UnicodeType, 0),
        }
