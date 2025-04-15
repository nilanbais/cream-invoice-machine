

from dataclasses import dataclass, field
from typing import List, Generic, TypeVar, Any, Optional

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
    
    def get_by_attribute(self, attr: str, value: Any) -> Optional[TYPE_PLACEHOLDER]:
        """
        Returns the first item in entries where getattr(item, attr) == value.
        Returns None if no match is found.
        """
        for item in self.entries:
            if getattr(item, attr, None) == value:
                return item
        return None




@dataclass
class InvoiceDetails:
    invoice_number: str
    date: str
    customer_name: str
    customer_address: str


@dataclass
class InvoiceLineItem:
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
class InvoiceCostItems(DataListBase[InvoiceLineItem]):
    """
    Represents a collection of InvoiceLineItem objects (also known as cost items),
    which together form the detailed breakdown of an invoice.
    This class establishes the relationship between individual cost items and the complete invoice structure.
    """
    pass


@dataclass
class CompanyDetails:
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
class CompanyList(DataListBase[CompanyDetails]):
    pass


# TODO: styling object toevoegen aan dataclass
@dataclass
class InvoiceTemplateInput:
    invoice_details: InvoiceDetails
    company_details: CompanyDetails
    invoice_items: InvoiceCostItems


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
class ClientDetails:
    name: str
    address: str
    post_code: str
    city: str


@dataclass
class JobCalculationDetails:
    btw_percentage: int  # x%
    round_up: int  # 10: 123 => 130 , 100: 167 => 200 
    extra_fixed: float


@dataclass
class JobDetailsInput:
    job_name: str
    date: str
    company_name: str
    client_info: ClientDetails
    work_details: dict
    calculation_info: JobCalculationDetails 
    

@dataclass
class InvoiceGeneratorConfigurations:
    file_format: str
    user_input_folder: str
    output_folder: str
    company_information_input: str
    labour_type_information_input: str



@dataclass
class StyleSettings:
    font: Optional[str] = None
    font_size: Optional[int] = None
    font_style: Optional[str] = None
    border: Optional[int] = None


@dataclass
class StyleSettingsInputPackage:
    general: Optional[StyleSettings] 
    header: Optional[StyleSettings]
    footer: Optional[StyleSettings]
    company_details: Optional[StyleSettings]
    invoice_details: Optional[StyleSettings]
    invoice_items: Optional[StyleSettings] 
    table: Optional[StyleSettings]