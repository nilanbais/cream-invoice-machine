"""
Scripts to test functionality of the pdf generator.
"""
import os
import unittest
from cream_invoice_machine.services.invoice_generator import (
    generate_invoice_pdf_on_path,
    InvoiceGenerator
    )


class TestPDFGenerator(unittest.TestCase):
    
    def test_generate_invoice_pdf_on_path(self) -> None:
        print(f"Running: {self._testMethodName}")
        input_file = "input\\test_input_1.yaml"
        output_file = "output\\test_generate_invoice_pdf_on_path.pdf"
        
        generate_invoice_pdf_on_path(input_file, output_file)

    def test_invoice_generator_class(self) -> None:
        generator = InvoiceGenerator()
        
        generator.generate_invoices_from_set_configuration(verbose=True)

    def test_invoice_generator() -> None:
        generator = InvoiceGenerator()
    
        generator.generate_invoices()

if __name__ == '__main__':
    unittest.main()