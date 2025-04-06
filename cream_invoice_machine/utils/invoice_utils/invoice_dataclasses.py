

from dataclasses import dataclass, field
from typing import List, Generic, TypeVar


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
class ProductDetails:
    name: str
    unit: str
    price: float
    ean_number: int

TYPE_PLACEHOLDER = TypeVar('T')

@dataclass
class DataListBase(Generic[TYPE_PLACEHOLDER]):
    entries: List[TYPE_PLACEHOLDER] = field(default_factory=list)

    def __init__(self, entries: List[TYPE_PLACEHOLDER] = []) -> None:
        self.entries = entries
    

@dataclass
class ProductDetailsList(DataListBase[ProductDetails]):
    pass


@dataclass
class JobInfo:
    name: str
    price: float
    unit: str

@dataclass
class JobTypeList:
    jobs: List[JobInfo]

    def __init__(self, jobs: List = []) -> None:
        self.jobs = jobs