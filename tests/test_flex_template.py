"""
Scripts to test functionality of the flex template for the pdf file.
"""
import unittest
from datetime import datetime


from cream_invoice_machine.templates.pdf import InvoicePDFTemplate

from cream_invoice_machine.models.dataclasses import InvoiceDetails, InvoiceCostItems, CompanyDetails
from cream_invoice_machine.utils.helper_functions import invoice_items_from_list


class TestFlexTemplate(unittest.TestCase):
    
    def testcase_setup(self) -> None:

        self.invoice_details: InvoiceDetails = InvoiceDetails(
            invoice_number="test invoice number 100",
            date='21-12-2024',
            customer_address='0223 woning 101B, 1010 SH Plaats',
            customer_name="de-nice"
        )
        self.invoice_items: InvoiceCostItems = invoice_items_from_list([
            {"description": "Stucwerk muren", "quantity": 20, "unit_price": 18.00, "total": 360},
            {"description": "Stucwerk plafond", "quantity": 15, "unit_price": 24.00, "total": 220},
        ])

        self.company_details: CompanyDetails = CompanyDetails(
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


    def test_pdf_template(self) -> None:
        self.testcase_setup()
        output_path = "output\\test_output_flex_template_test.pdf"
        InvoicePDFTemplate(self.invoice_details, self.company_details, self.invoice_items).render(output_path)


if __name__ == '__main__':
    unittest.main()