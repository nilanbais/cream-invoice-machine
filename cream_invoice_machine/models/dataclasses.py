

from dataclasses import dataclass, field
from typing import List, Generic, TypeVar

TYPE_PLACEHOLDER = TypeVar('T')


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
class InvoiceDetails:
    invoice_number: str
    date: str
    customer_name: str
    customer_address: str


@dataclass
class InvoiceCostItem:
    """
    Represents a single cost item on an invoice, also referred to as a line item.
    Each cost item includes a description, quantity, unit price, and the computed total.
    Cost items are the building blocks of an invoice and are grouped together within an InvoiceLineItems object.
    """
    description: str
    quantity: int
    unit_price: float
    total: int


@dataclass
class InvoiceLineItems(DataListBase[InvoiceCostItem]):
    """
    Represents a collection of InvoiceCostItem objects (also known as line items),
    which together form the detailed breakdown of an invoice.
    This class establishes the relationship between individual cost items and the complete invoice structure.
    """
    pass


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
    """
    Dataclass to hold the details of the reference data relating to the products that could be used to finish
    a job.
    """
    name: str
    unit: str
    price: float
    ean_number: int

@dataclass
class ProductDetailsList(DataListBase[ProductDetails]):
    pass


@dataclass
class LabourTypeInfo:
    """
    Dataclass to hold information relating to a standard type of labour that is needed to finish a job.
    """
    name: str
    price: float
    unit: str

@dataclass
class LabourTypeList(DataListBase[LabourTypeInfo]):
    pass


@dataclass
class InvoiceCalculationDetails:
    """
    Dataclass containing information that is needed to execute the calculation of an invoice for one job.
    """
    pass