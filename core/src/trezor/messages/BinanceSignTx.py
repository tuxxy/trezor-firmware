# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None  # type: ignore


class BinanceSignTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 704

    def __init__(
        self,
        address_n: List[int] = None,
        msg_count: int = None,
        account_number: int = None,
        chain_id: str = None,
        memo: str = None,
        sequence: int = None,
        source: int = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.msg_count = msg_count
        self.account_number = account_number
        self.chain_id = chain_id
        self.memo = memo
        self.sequence = sequence
        self.source = source

    @classmethod
    def get_fields(cls):
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('msg_count', p.UVarintType, 0),
            3: ('account_number', p.SVarintType, 0),
            4: ('chain_id', p.UnicodeType, 0),
            5: ('memo', p.UnicodeType, 0),
            6: ('sequence', p.SVarintType, 0),
            7: ('source', p.SVarintType, 0),
        }
