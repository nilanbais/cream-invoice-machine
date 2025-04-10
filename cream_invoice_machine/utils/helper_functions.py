from typing import List
from cream_invoice_machine.models.dataclasses import InvoiceCostItem, InvoiceLineItems


def flatten_list_of_dicts(input_list: List[dict]) -> dict:
    result: dict = {}
    for item in input_list:
        result.update(item)
    return result

def invoice_items_from_list(input_list: List[dict]) -> InvoiceLineItems:
    # Convert dictionaries to InvoiceItem instances
    invoice_items: List[InvoiceCostItem] = [InvoiceCostItem(**item) for item in input_list]
    return InvoiceLineItems(entries=invoice_items)