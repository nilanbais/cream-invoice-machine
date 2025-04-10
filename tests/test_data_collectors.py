"""
Scripts to test functionality of the data collector objects.
"""
import unittest
from datetime import datetime

from cream_invoice_machine.services.invoice_generator import render_invoice_pdf
from cream_invoice_machine.services.input_readers import (
    read_company_input,
    read_labour_type_input,
    read_job_input
)
from cream_invoice_machine.services.data_collectors import (
    collect_company_details,
    collect_invoice_details,
    collect_invoice_line_items
    )
from cream_invoice_machine.models.dataclasses import (
    CompanyDetails,
    InvoiceDetails,
    InvoiceCostItems
    )


class TestDataCollectorObjects(unittest.TestCase):

    def test_collect_company_details(self):
        path = "input\\test_input.yaml"

        company_input = read_company_input()
        job_details_input = read_job_input(file_path=path)

        collected_data: CompanyDetails = collect_company_details(
            company_input, 
            job_details_input
            )
        
        self.assertTrue(collected_data, None)
        self.assertTrue(isinstance(collected_data, CompanyDetails))

    def test_collect_invoice_details(self):
        path = "input\\test_input.yaml"

        job_details_input = read_job_input(file_path=path)

        collected_data: InvoiceDetails = collect_invoice_details(
            job_details_input
            )
        
        self.assertTrue(collected_data, None)
        self.assertTrue(isinstance(collected_data, InvoiceDetails))

    def test_collect_invoice_line_items(self):
        path = "input\\test_input.yaml"

        labour_type_input = read_labour_type_input()
        job_details_input = read_job_input(file_path=path)

        collected_data: InvoiceCostItems = collect_invoice_line_items(
            labour_type_input,
            job_details_input
            )
        
        self.assertTrue(collected_data, None)
        self.assertTrue(isinstance(collected_data, InvoiceCostItems))