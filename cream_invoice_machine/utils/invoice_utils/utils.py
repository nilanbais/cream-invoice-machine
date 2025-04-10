
from typing import List
from cream_invoice_machine.utils.invoice_utils.invoice_dataclasses import InvoiceCostItem, InvoiceLineItems

def invoice_items_from_list(input_list: List[dict]) -> InvoiceLineItems:
    # Convert dictionaries to InvoiceItem instances
    invoice_items: List[InvoiceCostItem] = [InvoiceCostItem(**item) for item in input_list]
    return InvoiceLineItems(entries=invoice_items)
