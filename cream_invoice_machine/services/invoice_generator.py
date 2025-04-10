"""
Sctipt containing the invoice generator. 

This class is responsible for handling the input data structure 
and call the correct functionality for generating the pdf pages.
"""

from cream_invoice_machine.services.data_collectors import collect_template_input
from cream_invoice_machine.templates.pdf import (
    InvoicePDF, 
    InvoicePDFTemplate, 
    TESTInvoicePDF
    )
from cream_invoice_machine.models.dataclasses import (
    InvoiceDetails, 
    InvoiceCostItems, 
    CompanyDetails,
    InvoiceTemplateInput,
    JobDetailsInput,
    LabourTypeList,
    CompanyList
    )
from cream_invoice_machine.services.input_readers import (
    read_job_input, 
    read_product_input, 
    read_company_input,
    read_labour_type_input
    )



def render_invoice_pdf(invoice_details: InvoiceDetails, invoice_items: InvoiceCostItems, company_details: CompanyDetails, output_path: str) -> InvoicePDF:
    InvoicePDFTemplate(invoice_details, company_details, invoice_items).render(output_path)


def render_pdf_object(pdf_object: InvoicePDFTemplate, output_path) -> None:
    pdf_object.render(output_path)


def generate_invoice_pdf_on_path(input_path: str, output_path: str) -> None:
    company_input: CompanyList = read_company_input()
    labour_type_input: LabourTypeList = read_labour_type_input()
    job_details_input: JobDetailsInput = read_job_input(file_path=input_path)

    invoice_generator_input_data: InvoiceTemplateInput = collect_template_input(
        company_input,
        labour_type_input,
        job_details_input
    )

    pdf_object: InvoicePDFTemplate = InvoicePDFTemplate(
        invoice_details=invoice_generator_input_data.invoice_details,
        company_details=invoice_generator_input_data.company_details,
        invoice_items=invoice_generator_input_data.invoice_items
    )

    render_pdf_object(pdf_object, output_path)


def invoice_generator_test(invoice_details: InvoiceDetails, invoice_items: InvoiceCostItems, output_path: str) -> InvoicePDF:
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