"""
Sctipt containing the invoice generator. 

This class is responsible for handling the input data structure 
and call the correct functionality for generating the pdf pages.
"""

from cream_invoice_machine.utils.invoice_utils.invoice_class import InvoicePDF, TESTInvoicePDF
from cream_invoice_machine.utils.invoice_utils.invoice_dataclasses import InvoiceDetails, InvoiceItems



def invoice_generator(invoice_details: InvoiceDetails, invoice_items: InvoiceItems, output_path: str) -> InvoicePDF:
    pdf_object = InvoicePDF()
    pdf_object.add_page()
    pdf_object.add_invoice_details(invoice_details)
    pdf_object.add_corp_details()
    pdf_object.add_invoice_items(invoice_items)
    pdf_object.output(output_path)


def invoice_generator_test(invoice_details: InvoiceDetails, invoice_items: InvoiceItems, output_path: str) -> InvoicePDF:
    pdf_object = TESTInvoicePDF()
    pdf_object.add_client_info(invoice_details.customer_name, invoice_details.customer_address)
    pdf_object.add_invoice_table(invoice_items)
    pdf_object.output(output_path)


# TODO - Denk of deze wel echt nodig is. Misschien is het beter om the class alle input data los aan te bieden.
def pdf_generator(input_data: dict) -> InvoicePDF:
    print("I create file yes please massage")

    # create pdf base
    pdf_object = InvoicePDF()
    # set font
    font_name = input_data["font-name"]
    font_path = input_data["font-path"]
    pdf_object.add_font(font_name, style="", fname=font_path)
    # add page
    pdf_object.add_page()
    # add invoice details
    pdf_object.add_invoice_details(
        invoice_number=input_data["invoice-number"],
        date=input_data["date"],
        customer_name=input_data["customer-name"],
        customer_address=input_data["customer-address"]
    )
    # add table
    pdf_object.add_table(input_data["items"])

    # store pdf_object
    pdf_object.output(input_data["output-path"])