

from dataclasses import dataclass, field
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


@dataclass
class ProductDetails:
    name: str
    unit: str
    price: float
    ean_number: int

@dataclass
class ProductDetailsList:
    items: List[ProductDetails]
    
    def __init__(self, items: List = []) -> None:
        self.items = items