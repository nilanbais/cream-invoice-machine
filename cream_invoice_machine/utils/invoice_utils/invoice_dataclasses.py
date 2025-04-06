

from dataclasses import dataclass, field
from typing import List, Generic, TypeVar

TYPE_PLACEHOLDER = TypeVar('T')

@dataclass
class InvoiceDetails:
    invoice_number: str
    date: str
    customer_name: str
    customer_address: str


@dataclass
class InvoiceItem:
    description: str
    quantity: int
    unit_price: float
    total: int


@dataclass
class InvoiceItems:
    items: List[InvoiceItem]


@dataclass
class CompDetails:
    name: str
    address: str
    postcode: str
    city: str
    phone: str
    email: str
    kvk_number: str
    btw_number: str
    iban: str


@dataclass
class DataListBase(Generic[TYPE_PLACEHOLDER]):
    """
    A generic base class for managing a list of typed entries.

    This class should be subclassed with a specific type provided for TYPE_PLACEHOLDER.
    For example: `class ProductList(DataListBase[Product])`.

    Attributes:
        entries (List[TYPE_PLACEHOLDER]): A list of items of a specified type. Defaults to an empty list.

    Methods:
        __init__(entries: List[TYPE_PLACEHOLDER] = []):
            Initializes the object with an optional list of entries.

        add(item: TYPE_PLACEHOLDER) -> None:
            Adds a single item to the entries list.
    """
    entries: List[TYPE_PLACEHOLDER] = field(default_factory=list)

    def __init__(self, entries: List[TYPE_PLACEHOLDER] = []) -> None:
        self.entries = entries

    def add(self, item: TYPE_PLACEHOLDER) -> None:
        self.entries.append(item)


@dataclass
class ProductDetails:
    name: str
    unit: str
    price: float
    ean_number: int

@dataclass
class ProductDetailsList(DataListBase[ProductDetails]):
    pass


@dataclass
class JobInfo:
    name: str
    price: float
    unit: str

@dataclass
class JobTypeList(DataListBase[JobInfo]):
    pass