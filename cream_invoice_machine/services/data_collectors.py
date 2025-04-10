"""
Scripts/functionality responsible for collection the data used as input
for generating one invoice.
"""
from datetime import datetime

from cream_invoice_machine.utils.helper_functions import flatten_nested_dict
from cream_invoice_machine.models.dataclasses import (
    InvoiceTemplateInput,
    InvoiceDetails,
    CompanyDetails, 
    CompanyList, 
    JobDetailsInput,
    LabourTypeList,
    JobDetailsInput,
    InvoiceCostItems,
    InvoiceLineItem
    )


def collect_template_input(
        company_input: CompanyList, 
        labour_type_input: LabourTypeList, 
        job_details_input: JobDetailsInput
        ) -> InvoiceTemplateInput:
    
    invoice_template_input = InvoiceTemplateInput(
        invoice_details=collect_invoice_details(job_details_input),
        company_details=collect_company_details(company_input, job_details_input),
        invoice_items=collect_invoice_line_items(labour_type_input, job_details_input)
    )
    return invoice_template_input
    


def collect_company_details(
        company_input: CompanyList,
        job_details_input: JobDetailsInput
        ) -> CompanyDetails:
    
    company_name: str = job_details_input.company_name

    company_details: CompanyDetails = company_input.get_by_attribute(attr="name", value=company_name)
    
    return company_details


def collect_invoice_details(
        job_details_input: JobDetailsInput
        ) -> InvoiceDetails:
    
    if job_details_input.date == 'auto':
        invoice_date = str(datetime.now().date())
    else:
        invoice_date = job_details_input.date
    
    full_address: str = str().join([
        job_details_input.client_info.address,
        ", ",
        job_details_input.client_info.post_code,
        " ",
        job_details_input.client_info.city
    ])

    invoice_details = InvoiceDetails(
        invoice_number="moet deze nog wel??",
        date=invoice_date,
        customer_name=job_details_input.client_info.name,
        customer_address=full_address
    )

    return invoice_details


def collect_invoice_line_items(
        labour_type_input: LabourTypeList, 
        job_details_input: JobDetailsInput
        ) -> InvoiceCostItems:
    
    work_input: dict = job_details_input.work_details

    invoice_cost_item_list: InvoiceCostItems = InvoiceCostItems()

    for work_type, work_item in work_input.items():
        labour_type_info_ref = labour_type_input.get_by_attribute(attr="name", value=work_type)
        if isinstance(work_item, dict):
            for nested_key, nested_value in work_item.items():
                description = str().join([work_type, ' - ', nested_key])
                line_item = InvoiceLineItem(
                    description=description,
                    quantity=nested_value,
                    unit_price=labour_type_info_ref.price,
                    total=(nested_value*labour_type_info_ref.price)
                )
                invoice_cost_item_list.add(line_item)
        else:
            line_item = InvoiceLineItem(
                description=work_type,
                quantity=work_item,
                unit_price=labour_type_info_ref.price,
                total=(work_item*labour_type_info_ref.price)
            )
            invoice_cost_item_list.add(line_item)
        
    return invoice_cost_item_list