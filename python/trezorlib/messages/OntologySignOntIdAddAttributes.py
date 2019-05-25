# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .OntologyOntIdAddAttributes import OntologyOntIdAddAttributes
from .OntologyTransaction import OntologyTransaction

if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None  # type: ignore


class OntologySignOntIdAddAttributes(p.MessageType):
    MESSAGE_WIRE_TYPE = 360

    def __init__(
        self,
        address_n: List[int] = None,
        transaction: OntologyTransaction = None,
        ont_id_add_attributes: OntologyOntIdAddAttributes = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.transaction = transaction
        self.ont_id_add_attributes = ont_id_add_attributes

    @classmethod
    def get_fields(cls):
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('transaction', OntologyTransaction, 0),
            3: ('ont_id_add_attributes', OntologyOntIdAddAttributes, 0),
        }
