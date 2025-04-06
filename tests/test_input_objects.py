"""
Scripts to test functionality of the flex template for the pdf file.
"""
import unittest
from datetime import datetime

from cream_invoice_machine.utils.invoice_generator import invoice_generator
from cream_invoice_machine.utils.input_objects import CompanyInfoInput


class TestInputObject(unittest.TestCase):
    
    def testcase_setup(self) -> None:
        self.output_file = "output\\test_output_flex_template_test.pdf"
        self.new_path = 'resources\\product_info.yaml'

    def test_corp_input_object_auto_read(self) -> None:
        self.testcase_setup()
        test_obj = CompanyInfoInput(auto_read=True)
        self.assertTrue(test_obj._raw_data, None)

    def test_corp_input_path_change(self) -> None:
        self.testcase_setup()
        test_obj = CompanyInfoInput()
        original_path = test_obj._file_path

        test_obj.set_input_file_path(new_path=self.new_path)
        new_path = test_obj._file_path

        self.assertTrue(new_path, None)
        self.assertNotEqual(new_path, original_path)

    def test_corp_input_set_data(self) -> None:
        self.testcase_setup()
        test_obj = CompanyInfoInput(auto_read=True)

        test_obj.set_corp_invoice_details()

        self.assertTrue(test_obj._company_details, None)
        print(test_obj.CompDetails)

if __name__ == '__main__':
    unittest.main()