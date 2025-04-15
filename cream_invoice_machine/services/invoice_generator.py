"""
Sctipt containing the invoice generator. 

This class is responsible for handling the input data structure 
and call the correct functionality for generating the pdf pages.
"""
import os
from datetime import datetime

from cream_invoice_machine.services.data_collectors import collect_template_input
from cream_invoice_machine.utils.file_readers import read_env_variable
from cream_invoice_machine.utils.helper_functions import (
    list_files,
    basename_from_path
    )
from cream_invoice_machine.templates.pdf import (
    InvoicePDF, 
    InvoicePDFTemplate
    )
from cream_invoice_machine.models.dataclasses import (
    InvoiceDetails, 
    InvoiceCostItems, 
    CompanyDetails,
    InvoiceTemplateInput,
    JobDetailsInput,
    LabourTypeList,
    CompanyList,
    InvoiceGeneratorConfigurations,
    DataListBase
    )
from cream_invoice_machine.services.input_readers import (
    read_job_input, 
    read_product_input, 
    read_company_input,
    read_labour_type_input
    )



def render_invoice_pdf(invoice_details: InvoiceDetails, invoice_items: InvoiceCostItems, company_details: CompanyDetails, output_path: str) -> None:
    InvoicePDFTemplate(invoice_details, company_details, invoice_items).render(output_path)


def render_pdf_object(pdf_object: InvoicePDFTemplate, output_path) -> None:
    pdf_object.render(output_path)


def generate_invoice_pdf_on_path(input_path: str, output_path: str) -> None:
    company_input: CompanyList = read_company_input(read_env_variable("DEFAULT_COMPANY_INFO_PATH"))
    labour_type_input: LabourTypeList = read_labour_type_input(read_env_variable("DEFAULT_LABOUR_TYPE_INFO_PATH"))
    job_details_input: JobDetailsInput = read_job_input(file_path=input_path)

    invoice_generator_input_data: InvoiceTemplateInput = collect_template_input(
        company_input,
        labour_type_input,
        job_details_input
    )

    pdf_object: InvoicePDFTemplate = InvoicePDFTemplate(
        invoice_details=invoice_generator_input_data.invoice_details,
        company_details=invoice_generator_input_data.company_details,
        invoice_items=invoice_generator_input_data.invoice_items
    )

    render_pdf_object(pdf_object, output_path)


class InvoiceGenerator:

    def __init__(self) -> None:
        # auto set default configuration
        self.set_generator_configurations()

    def set_generator_configurations(
            self, 
            file_format: str = 'pdf',
            user_input_folder: str = 'default',
            output_folder: str = 'default',
            styling_input_path: str = ' default',
            company_information_input_path: str = 'default',
            labour_type_information_input_path: str = 'default'
            ) -> None:
        
        file_format = '.' + file_format if '.' not in file_format else file_format
        user_input_folder: str = self._get_default_user_input_folder() if user_input_folder == 'default' else user_input_folder
        output_folder: str = self._get_default_output_folder() if output_folder == 'default' else output_folder
        styling_input_path: str = self._get_default_styling_input_path() if styling_input_path == 'default' else styling_input_path
        company_information_input_path: str = self._get_default_company_information_path() if company_information_input_path == 'default' else company_information_input_path
        labour_type_information_input_path: str = self._get_default_labour_type_information_path() if labour_type_information_input_path == 'default' else labour_type_information_input_path

        self._generator_cofiguration = InvoiceGeneratorConfigurations(
            file_format=file_format,
            user_input_folder=user_input_folder,
            output_folder=output_folder,
            document_styling_input=styling_input_path,
            company_information_input=company_information_input_path,
            labour_type_information_input=labour_type_information_input_path
        )
    
    @property
    def configurations(self) -> InvoiceGeneratorConfigurations:
        return self._generator_cofiguration

    @staticmethod
    def _get_default_user_input_folder() -> str:
        return read_env_variable("DEFAULT_INPUT_FOLDER_PATH")
    
    @staticmethod
    def _get_default_output_folder() -> str:
        return read_env_variable("DEFAULT_OUTPUT_FOLDER_PATH")
    
    @staticmethod
    def _get_default_styling_input_path() -> str:
        return read_env_variable("DEFAULT_STYLEING_INPUT_PATH")
    
    @staticmethod
    def _get_default_company_information_path() -> str:
        return read_env_variable("DEFAULT_COMPANY_INFO_PATH")

    @staticmethod
    def _get_default_labour_type_information_path() -> str:
        return read_env_variable("DEFAULT_LABOUR_TYPE_INFO_PATH")
    
    @staticmethod
    def _render_filename_from_path(path: str) -> str:
        basename: str = basename_from_path(path)
        if '.' in basename:
            # drop file format like '.yaml' from basename
            basename = basename.split('.')[0]

        today_str = datetime.today().strftime("%d_%m_%Y")
        render_filename: str = str().join([f"render_{today_str}_", basename])
        return render_filename

    def generate_invoices_from_set_configuration(self, verbose: bool = False) -> None:
        # get list of input files
        input_files: list = list_files(os.path.abspath(self.configurations.user_input_folder))
        
        company_info_input: DataListBase = read_company_input(self.configurations.company_information_input)
        labour_type_input: DataListBase = read_labour_type_input(self.configurations.labour_type_information_input)

        for file_path in input_files:

            if verbose:
                print("Now working on file:", file_path)

            job_information: JobDetailsInput = read_job_input(file_path)

            invoice_template_input: InvoiceTemplateInput = collect_template_input(
                company_input=company_info_input,
                labour_type_input=labour_type_input,
                job_details_input=job_information
                )
            
            invoice_document = InvoicePDFTemplate(
                input_package=invoice_template_input
                )


            output_path: str = os.path.join(
                os.path.abspath(self.configurations.output_folder),
                self._render_filename_from_path(file_path) + self.configurations.file_format
                )
            
            if verbose:
                print("rendering pdf document for output:", output_path)

            invoice_document.render(output_path)