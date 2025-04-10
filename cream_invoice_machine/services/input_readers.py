"""
Scripts responsible for reading and ordening input data
"""

from datetime import datetime

from cream_invoice_machine.utils.file_readers import read_yaml, read_env_variable
from cream_invoice_machine.models.dataclasses import (
    CompanyDetails,
    CompanyList,
    ProductDetails, 
    ProductDetailsList, 
    LabourTypeInfo, 
    LabourTypeList, 
    JobDetailsInput,
    ClientDetails,
    JobCalculationDetails
    )



def read_company_input(file_path: str = None) -> CompanyList:
    if file_path:
        raw_data: dict = read_yaml(file_path)
    else:
        raw_data: dict = read_yaml(read_env_variable("COMPANY_INFO_PATH"))

    company_list: CompanyList = CompanyList()

    for company_name, company_details in raw_data.items():
        input_data: CompanyDetails = CompanyDetails(
            name=company_name,
            address=company_details['adres'],
            postcode=company_details['postcode'],
            city=company_details['plaats'],
            phone=company_details['telefoon'],
            email=company_details['email'],
            kvk_number=company_details['kvk-nummer'],
            btw_number=company_details['btw-nummer'],
            iban=company_details['iban']
        )
        company_list.add(input_data)

    return company_list


def read_product_input(file_path: str = None) -> ProductDetailsList:
    if file_path:
        raw_data: dict = read_yaml(file_path)
    else:
        raw_data: dict = read_yaml(read_env_variable("PRODUCT_INFO_PATH"))

    products_list: ProductDetailsList = ProductDetailsList()

    for product_name, product_info in raw_data.items():

        item_details = ProductDetails(
            name=product_name,
            unit=product_info['unit'],
            price=product_info['prijs'],
            ean_number=product_info['EAN nummer']
        )

        products_list.add(item_details)
    
    return products_list


def read_labour_type_input(file_path: str = None) -> LabourTypeList:
    if file_path:
        raw_data: dict = read_yaml(file_path)
    else:
        raw_data: dict = read_yaml(read_env_variable("LABOUR_TYPE_INFO_PATH"))

    labour_type_list: LabourTypeList = LabourTypeList()
    for labour_type, labour_type_details in raw_data.items():
        item_details = LabourTypeInfo(
            name=labour_type,
            unit=labour_type_details['unit'],
            price=labour_type_details['prijs']
        )
        labour_type_list.add(item_details)
    return labour_type_list


def read_job_input(file_path: str) -> JobDetailsInput:
    raw_data: dict = read_yaml(file_path)

    raw_client_data = raw_data['klant-info']
    raw_work_data = raw_data['werk']
    raw_calc_info_data = raw_data['extra']

    job_details_input = JobDetailsInput(
        job_name=raw_data['invoice'],
        date=raw_data['date'],
        company_name=raw_data['uitvoerder'],
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

