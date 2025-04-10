"""
Scripts to test functionality of the file reader.
"""
import unittest
from cream_invoice_machine.utils.file_readers import read_yaml, read_env_variable

class TestFileReader(unittest.TestCase):
    
    def testcase_setup(self) -> None:
        self.input_file = "input\\test_input.yaml"

    def test_generating_pdf_expected_input(self) -> None:
        print(f"Running: {self._testMethodName}")
        self.testcase_setup()
        test_result = read_yaml(path=self.input_file)
        self.assertTrue(test_result, None)
        print(test_result)

    def test_reading_env_variables(self) -> None:
        print(f"Running: {self._testMethodName}")
        test_result: str = read_env_variable("CORP_INFO_PATH")
        self.assertTrue(test_result, None)


if __name__ == '__main__':
    unittest.main()