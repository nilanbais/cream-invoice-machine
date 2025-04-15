
import unittest

from cream_invoice_machine.utils.helper_functions import (
    list_files, 
    basename_from_path,
    style_settings_from_dict
    )

class TestHelperFunctions(unittest.TestCase):

    def test_list_user_input_files(self) -> None:
        input_folder = "input\\"
        test_result: list = list_files(input_folder)
        
        print("test_result", test_result)

    def test_basename_from_path(self) -> None:
        input_path: str = "C:\\Users\\NilanBais\\Documents\\Github\\cream-invoice-machine\\resources\\labour_type_info.yaml"
        test_result: list = basename_from_path(input_path)
        
        print("test_result", test_result)
        assert test_result == 'labour_type_info.yaml', "result no good. go see: {}".format(test_result)

    def test_style_settings_from_dict(self) -> None:
        input_dict: dict = {'font': 'Helvetica'}
        
        test_result: list = style_settings_from_dict(input_dict)
        
        print("test_result", test_result)


if __name__ == '__main__':
    unittest.main()
