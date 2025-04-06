

from dataclasses import dataclass
from typing import List


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
