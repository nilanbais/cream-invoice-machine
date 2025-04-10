
from typing import List
from cream_invoice_machine.utils.invoice_utils.invoice_dataclasses import InvoiceItem, InvoiceItems

def invoice_items_from_list(input_list: List[dict]) -> InvoiceItems:
    # Convert dictionaries to InvoiceItem instances
    invoice_items: List[InvoiceItem] = [InvoiceItem(**item) for item in input_list]
    return InvoiceItems(entries=invoice_items)
