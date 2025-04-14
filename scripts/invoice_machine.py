"""
Script to orchestrate the reading of the input, generating an invoice, and storing 
the output. This file will be ONLY calling functions and parsing their results.

Step to partake:
- Call functions to retrieve the input files
- Call function to generate the file, with a given input from input files
- Call function to store the give result
- Exception handling to make noticable is something (or some input) didn't go well
"""
from cream_invoice_machine.services.invoice_generator import InvoiceGenerator

def main() -> None:
    # config env variables (oragisation info among other standard variables)
    generator = InvoiceGenerator()
    
    generator.generate_invoices_from_set_configuration()


if __name__ == "__main__":
    main()