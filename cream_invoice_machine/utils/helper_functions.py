from typing import List

from datetime import datetime

from cream_invoice_machine.models.dataclasses import (
    InvoiceLineItem, 
    InvoiceCostItems,
    JobDetailsInput,
    ClientDetails,
    JobCalculationDetails
    )


def flatten_list_of_dicts(input_list: List[dict]) -> dict:
    result: dict = {}
    for item in input_list:
        result.update(item)
    return result


def flatten_nested_dict(input_dict: dict) -> dict:
    result: dict = {}
    for key, value in input_dict.items():
        if isinstance(value, dict):
            for nested_key, nested_value in value.items():
                new_key = str().join([key, ' - ', nested_key])
                result[new_key] = nested_value
        else:
            result[key] = value
    return result


def invoice_items_from_list(input_list: List[dict]) -> InvoiceCostItems:

    # Convert dictionaries to InvoiceItem instances
    invoice_items: List[InvoiceLineItem] = [InvoiceLineItem(**item) for item in input_list]
    return InvoiceCostItems(entries=invoice_items)


def job_details_from_yaml_data(yaml_data: dict) -> JobDetailsInput:
    raw_data = yaml_data

    if raw_data['date'] == 'auto':
        invoice_date = str(datetime.now().date())
    else:
        invoice_date = raw_data['date']

    raw_client_data = raw_data['klant-info']
    raw_work_data = raw_data['werk']
    raw_calc_info_data = raw_data['extra']

    job_details_input = JobDetailsInput(
        job_name=raw_data['invoice'],
        date=invoice_date,
        client_info=ClientDetails(
            name=raw_client_data['naam'],
            address=raw_client_data['adres'],
            post_code=raw_client_data['postcode'],
            city=raw_client_data['plaats']
        ),
        work_details=raw_work_data,
        calculation_info=JobCalculationDetails(
            btw_percentage=raw_calc_info_data['btw'],
            round_up=raw_calc_info_data['onvoorzien']['afronding'],
            extra_fixed=raw_calc_info_data['onvoorzien']['bijtelling']
        )
    )

    return job_details_input