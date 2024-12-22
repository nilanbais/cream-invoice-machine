"""
Scripts to orchestrate reading and preparing the input variables.

This includes the input .yaml-files
"""
import os
from datetime import datetime

from cream_invoice_machine.utils.file_reader import read_yaml, read_env_variable
from cream_invoice_machine.utils.invoice_utils.invoice_dataclasses import CorpInvoiceDetails


class CorpInfoInput:

    _file_path: str = read_env_variable("CORP_INFO_PATH")
    _raw_data: dict = None
    _invoice_details: CorpInvoiceDetails = None

    def __init__(self, auto_read: bool = False):
        if auto_read:
            print(self._file_path, type(self._file_path))
            self._read_input()

    def set_input_file_path(self, new_path: str) -> None:
        self._file_path = new_path

    def _read_input(self) -> None:
        self._raw_data = read_yaml(self._file_path)

    def set_corp_invoice_details(self) -> None:
        self._invoice_details = CorpInvoiceDetails(
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
    def CorpInvoiceDetails(self) -> CorpInvoiceDetails:
        return self._invoice_details
    

class ProductInfoInput:

    _file_path: str = read_env_variable("PRODUCT_INFO_PATH")
    _raw_data: dict = None

    def __init__(self, auto_read: bool = False):
        if auto_read:
            print(self._file_path, type(self._file_path))
            self._read_input()

    def set_input_file_path(self, new_path: str) -> None:
        self._file_path = new_path

    def _read_input(self) -> None:
        self._raw_data = read_yaml(self._file_path)



class JobInfoInput:

    _file_path: str = None
    _raw_data: dict = None

    def __init__(self, auto_read: bool = False):
        pass
    
    def set_input_file_path(self, new_path: str) -> None:
        self._file_path = new_path

    def _read_input(self) -> None:
        self._raw_data = read_yaml(self._file_path)