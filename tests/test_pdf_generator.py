"""
Scripts to test functionality of the pdf generator.
"""
import os
import unittest
from cream_invoice_machine.services.invoice_generator import (
    render_invoice_pdf, 
    invoice_generator_test,
    generate_invoice_pdf_on_path,
    InvoiceGenerator
    )
from cream_invoice_machine.models.dataclasses import InvoiceDetails, InvoiceCostItems, CompanyDetails
from cream_invoice_machine.utils.input_objects import CompanyInfoInput
from cream_invoice_machine.utils.helper_functions import invoice_items_from_list


class TestPDFGenerator(unittest.TestCase):
    
    def test_generate_invoice_pdf_on_path(self) -> None:
        print(f"Running: {self._testMethodName}")
        input_file = "input\\test_input_1.yaml"
        output_file = "output\\test_generate_invoice_pdf_on_path.pdf"
        
        generate_invoice_pdf_on_path(input_file, output_file)

    def test_invoice_generator_class(self) -> None:
        generator = InvoiceGenerator()
        
        generator.generate_invoices_from_set_configuration(verbose=True)

if __name__ == '__main__':
    unittest.main()