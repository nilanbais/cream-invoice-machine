"""
Scripts to test functionality of the pdf generator.
"""
import unittest
from cream_invoice_machine.utils.invoice_generator import invoice_generator
from cream_invoice_machine.utils.invoice_utils.invoice_dataclasses import InvoiceDetails, InvoiceItems, invoice_items_from_list


class TestPDFGenerator(unittest.TestCase):
    
    def testcase_setup(self) -> None:
        self.input_file = ""
        self.output_file = "output\\test_output_flex_template_test.pdf"
        self.invoice_details = InvoiceDetails(
            invoice_number="test invoice number 100",
            date='21-12-2024',
            customer_address='0223 woning 101B, 1010 SH Fuck Texel test',
            customer_name="de-nice"
        )
        self.items: InvoiceItems = invoice_items_from_list([
            {"description": "Stucwerk muren", "quantity": 20, "price": 18.00},
            {"description": "Stucwerk plafond", "quantity": 15, "price": 24.00},
        ])

    def test_generating_pdf_expected_input(self) -> None:
        self.testcase_setup()
        invoice_generator(
            invoice_details=self.invoice_details, 
            invoice_items=self.items,
            output_path=self.output_file
        )



if __name__ == '__main__':
    unittest.main()