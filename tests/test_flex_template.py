"""
Scripts to test functionality of the flex template for the pdf file.
"""
import unittest
from datetime import datetime

from cream_invoice_machine.utils.invoice_generator import invoice_generator

class TestFlexTemplate(unittest.TestCase):
    
    def testcase_setup(self) -> None:
        self.output_file = "output\\test_output_flex_template_test.pdf"

    def test_pdf_template(self) -> None:
        self.testcase_setup()



if __name__ == '__main__':
    unittest.main()