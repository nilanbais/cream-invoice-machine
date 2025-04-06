"""
Scripts to test functionality of the pdf generator.
"""
import unittest
from cream_invoice_machine.utils.invoice_generator import invoice_generator, invoice_generator_test
from cream_invoice_machine.utils.invoice_utils.invoice_dataclasses import InvoiceDetails, InvoiceItems, CompDetails
from cream_invoice_machine.utils.invoice_utils.utils import invoice_items_from_list


class TestPDFGenerator(unittest.TestCase):
    
    def testcase_setup(self) -> None:
        self.input_file = ""
        self.output_file = "output\\test_output_flex_template_test.pdf"
        
        self.invoice_details = InvoiceDetails(
            invoice_number="test invoice number 100",
            date='21-12-2024',
            customer_address='0223 woning 101B, 1010 SH Fuck Texel',
            customer_name="de-nice"
        )
        self.items: InvoiceItems = invoice_items_from_list([
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
        self.testcase_setup()
        invoice_generator(
            invoice_details=self.invoice_details, 
            invoice_items=self.items,
            company_details=self.company_details,
            output_path=self.output_file
        )



if __name__ == '__main__':
    unittest.main()