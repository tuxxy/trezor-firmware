# Automatically generated by pb2py
# fmt: off
import protobuf as p


class BinanceSignedTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 709

    def __init__(
        self,
        signature: bytes = None,
        public_key: bytes = None,
        json: str = None,
    ) -> None:
        self.signature = signature
        self.public_key = public_key
        self.json = json

    @classmethod
    def get_fields(cls):
        return {
            1: ('signature', p.BytesType, 0),
            2: ('public_key', p.BytesType, 0),
            3: ('json', p.UnicodeType, 0),
        }
