"""
Scripts to orchestrate reading and preparing the input variables.

This includes the input .yaml-files
"""
import os
from datetime import datetime
from abc import ABC, abstractmethod

from cream_invoice_machine.utils.file_reader import read_yaml, read_env_variable
from cream_invoice_machine.utils.helper_functions import flatten_list_of_dicts
from cream_invoice_machine.utils.invoice_utils.invoice_dataclasses import CompDetails, ProductDetails, ProductDetailsList, JobInfo, JobTypeList


class InfoInputObjectBase(ABC):

    @property
    @abstractmethod
    def _file_path(self):
        ...

    @property
    @abstractmethod
    def object_details(self):
        ...

    @abstractmethod
    def set_object_details(self) -> None:
        ...

    def set_input_file_path(self, new_path: str) -> None:
        self._file_path = new_path


class CompanyInfoInput(InfoInputObjectBase):

    _file_path: str = read_env_variable("COMPANY_INFO_PATH")
    _raw_data: dict = None
    _company_details: CompDetails = None

    def __init__(self, auto_read: bool = False):
        if auto_read:
            self._read_input()
            self.set_object_details()

    def _read_input(self) -> None:
        self._raw_data = read_yaml(self._file_path)

    def set_object_details(self) -> None:
        self._company_details = CompDetails(
            name=self._raw_data['naam'],
            address=self._raw_data['adres'],
            postcode=self._raw_data['postcode'],
            city=self._raw_data['plaats'],
            phone=self._raw_data['telefoon'],
            email=self._raw_data['email'],
            kvk_number=self._raw_data['kvk-nummer'],
            btw_number=self._raw_data['btw-nummer'],
            iban=self._raw_data['iban']
        )
    
    @property
    def object_details(self) -> CompDetails:
        return self._company_details
    

class ProductInfoInput(InfoInputObjectBase):

    _file_path: str = read_env_variable("PRODUCT_INFO_PATH")
    _raw_data: dict = None
    object_details: ProductDetailsList = ProductDetailsList()

    def __init__(self, auto_read: bool = False):
        if auto_read:
            self._read_input()
            self.set_object_details()

    def _read_input(self) -> None:
        self._raw_data = read_yaml(self._file_path)

    def set_object_details(self) -> None:
        for product_name, product_info in self._raw_data.items():
            product_info: dict = flatten_list_of_dicts(product_info)
            item_details = ProductDetails(
                name=product_name,
                unit=product_info['unit'],
                price=product_info['prijs'],
                ean_number=product_info['EAN nummer']
            )
            self.object_details.add(item_details)



class JobInfoInput(InfoInputObjectBase):

    _file_path: str = read_env_variable("JOB_INFO_PATH")
    _raw_data: dict = None
    object_details: JobTypeList = JobTypeList()

    def __init__(self, auto_read: bool = False):
        if auto_read:
            self._read_input()
            self.set_object_details()

    def _read_input(self) -> None:
        self._raw_data = read_yaml(self._file_path)

    def set_object_details(self) -> None:
        for job_name, job_info in self._raw_data.items():
            job_info: dict = flatten_list_of_dicts(job_info)
            item_details = JobInfo(
                name=job_name,
                unit=job_info['unit'],
                price=job_info['prijs']
            )
            self.object_details.add(item_details)