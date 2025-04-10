"""
Scripts to test functionality of the pdf generator.
"""
import os
import unittest
from cream_invoice_machine.services.invoice_generator import render_invoice_pdf, invoice_generator_test
from cream_invoice_machine.models.dataclasses import InvoiceDetails, InvoiceLineItems, CompDetails
from cream_invoice_machine.utils.input_objects import CompanyInfoInput
from cream_invoice_machine.utils.helper_functions import invoice_items_from_list


class TestPDFGenerator(unittest.TestCase):
    
    def testcase_setup(self) -> None:
        self.input_file = ""

        self.invoice_details: InvoiceDetails = InvoiceDetails(
            invoice_number="test invoice number 100",
            date='21-12-2024',
            customer_address='0223 woning 101B, 1010 SH Plaats',
            customer_name="de-nice"
        )
        self.items: InvoiceLineItems = invoice_items_from_list([
            {"description": "Stucwerk muren", "quantity": 20, "unit_price": 18.00, "total": 360},
            {"description": "Stucwerk plafond", "quantity": 15, "unit_price": 24.00, "total": 220},
        ])

        self.company_details: CompDetails = CompDetails(
            name="test test comp",
            address="test address",
            postcode="test postcode",
            city="test city",
            phone="test phone",
            email="test email",
            kvk_number="test kvk_number",
            btw_number="test btw_number",
            iban="test iban",
        )

    def test_generating_pdf_expected_input(self) -> None:
        print(f"Running: {self._testMethodName}")
        print("working dir", os.getcwd())
        self.testcase_setup()
        self.output_file = "output\\test_generating_pdf_expected_input_output.pdf"
        render_invoice_pdf(
            invoice_details=self.invoice_details, 
            invoice_items=self.items,
            company_details=self.company_details,
            output_path=self.output_file
        )

    def test_generating_pdf_with_yaml_files(self) -> None:
        print(f"Running: {self._testMethodName}")
        self.testcase_setup()
        self.output_file = "output\\test_generating_pdf_with_yaml_files_output.pdf"
        
        company_details = CompanyInfoInput(auto_read=True)
        
        render_invoice_pdf(
            invoice_details=self.invoice_details, 
            invoice_items=self.items,
            company_details=company_details.object_details,
            output_path=self.output_file
        )



if __name__ == '__main__':
    unittest.main()