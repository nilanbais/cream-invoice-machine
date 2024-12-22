

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
    price: float

@dataclass
class InvoiceItems:
    items: List[InvoiceItem]

@dataclass
class CorpDetails:
    name: str
    address: str
    postcost: str
    city: str
    phone: str
    email: str
    kvk_number: str
    btw_number: str
    iban: str


def invoice_items_from_list(input_list: List[dict]) -> InvoiceItems:
    # Convert dictionaries to InvoiceItem instances
    invoice_items = [InvoiceItem(**item) for item in input_list]
    return InvoiceItems(items=invoice_items)
    