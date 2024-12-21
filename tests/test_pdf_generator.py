"""
Scripts to test functionality of the pdf generator.
"""
import unittest
from cream_invoice_machine.utils.invoice_utils.invoice_generator import pdf_generator


class TestPDFGenerator(unittest.TestCase):
    
    def testcase_setup(self) -> None:
        self.input_file = ""
        self.output_file = ""
        self.input_data = {
            "hello": "massage",
            "yes": "please"
        }

    def test_generating_pdf_expected_input(self) -> None:
        self.testcase_setup()
        test_result = pdf_generator(input_data=self.input_data)



if __name__ == '__main__':
    unittest.main()