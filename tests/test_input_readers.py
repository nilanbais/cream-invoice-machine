
import unittest

from cream_invoice_machine.models.dataclasses import (
    CompanyList, 
    ProductDetailsList, 
    LabourTypeList,
    JobDetailsInput,
    StyleSettingsInputPackage
    )

from cream_invoice_machine.services.input_readers import (
    read_company_input, 
    read_product_input, 
    read_labour_type_input, 
    read_job_input,
    read_styling_settings
    )


class TestCompanyInputObject(unittest.TestCase):

    def test_read_company_input(self) -> None:
        print(f"Running: {self._testMethodName}")
        
        input_path: str = "resources\\company_info.yaml"

        test_object: CompanyList = read_company_input(input_path)

        self.assertTrue(test_object)
        self.assertTrue(isinstance(test_object, CompanyList))

    def test_read_product_input(self) -> None:
        print(f"Running: {self._testMethodName}")

        input_path: str = "resources\\product_info.yaml"

        test_object: ProductDetailsList = read_product_input(input_path)
        
        self.assertTrue(test_object)
        self.assertTrue(isinstance(test_object, ProductDetailsList))

    def test_read_labour_type_input(self) -> None:
        print(f"Running: {self._testMethodName}")
        
        input_path: str = "resources\\labour_type_info.yaml"

        test_object: LabourTypeList = read_labour_type_input(input_path)
       
        self.assertTrue(test_object)
        self.assertTrue(isinstance(test_object, LabourTypeList))

    def test_read_job_input(self) -> None:
        print(f"Running: {self._testMethodName}")

        input_path: str = "input\\test_input_1.yaml"

        test_object: JobDetailsInput = read_job_input(input_path)

        print("test_object", test_object)
        
        self.assertTrue(test_object)
        self.assertTrue(isinstance(test_object, JobDetailsInput))

    def test_read_styling_settings(self) -> None:
        print(f"Running: {self._testMethodName}")

        input_path: str = "resources\\styling_settings.yaml"

        test_object: StyleSettingsInputPackage = read_styling_settings(input_path)

        print("test_object", test_object)
        
        self.assertTrue(test_object)
        self.assertTrue(isinstance(test_object, StyleSettingsInputPackage))