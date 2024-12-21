"""
Scripts to test functionality of the file reader.
"""
import unittest
from cream_invoice_machine.utils.file_reader import read_yaml

class TestPDFGenerator(unittest.TestCase):
    
    def testcase_setup(self) -> None:
        self.input_file = "input\\test_input.yaml"

    def test_generating_pdf_expected_input(self) -> None:
        self.testcase_setup()
        test_result = read_yaml(path=self.input_file)
        self.assertTrue(test_result, None)
        print(test_result)



if __name__ == '__main__':
    unittest.main()