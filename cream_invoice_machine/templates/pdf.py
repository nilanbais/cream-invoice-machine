"""
Sctipt containing the invoice class. 

This class is responsible for and implements the structure of 
the generated pdf pages.
"""
from datetime import datetime, timedelta

from fpdf import FPDF, XPos, YPos

from typing import Optional

from cream_invoice_machine.templates.flex_template_test import InvoiceHeaderTemplate
from cream_invoice_machine.models.dataclasses import (
    InvoiceDetails,
    InvoiceCostItems, 
    CompanyDetails, 
    InvoiceTemplateInput,
    StyleSettingsInputPackage
    )




class InvoicePDF(FPDF):
    def __init__(self, orientation = "portrait", unit = "mm", format = "A4", font_cache_dir = "DEPRECATED"):
        super().__init__(orientation, unit, format, font_cache_dir)
        

    def header(self):
        # Bedrijfsnaam
        self.set_font('Helvetica', '', 12)
        self.image('resources\\logo\\logo_white.png', 10, 8, 33)  # Adjust the path and size as needed
        self.cell(0, 10, "Factuur",  new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(10)  # Lijnbreuk

    def footer(self):
        # Pagina-nummer
        self.set_y(-30)
        self.set_font('Helvetica', '', 8)
        self.multi_cell(0, 10, 
            "Te betalen binnen 30 dagen (voor DD-MM-YYYY) op rekeningnummer NL12BANK0123456789\n"
            "t.n.v. STUKADOORSBEDRIJF onder vermelding van klantnummer en factuurnummer.", 
            align='C'
        )
        self.cell(0, 10, f"Pagina {self.page_no()}", align="C")

    def add_invoice_details(self, invoice_details: InvoiceDetails):
        self.set_font('Helvetica', '', 10)
        self.cell(100, 10, f"Factuurnummer: {invoice_details.invoice_number}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(100, 10, f"Datum: {invoice_details.date}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(100, 10, f"Naam klant: {invoice_details.customer_name}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(100, 10, f"Adres klant: {invoice_details.customer_address}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(10)

    def add_company_details(self, company_details: CompanyDetails):
        self.set_font('Helvetica', 'B', 8)
        self.set_xy(140, 20)
        self.multi_cell(0, 8, 
            f"{company_details.name}\n"
            f"{company_details.address}\n"
            f"{company_details.postcode}, {company_details.city}\n"
            f"{company_details.phone}\n"
            f"{company_details.email}\n"
            f"{company_details.kvk_number}\n"
            f"{company_details.btw_number}\n"
            f"{company_details.iban}",
            align='L'
        )

    def add_invoice_items(self, invoice_items: InvoiceCostItems):
        self.set_xy(10, 100)
        # Header for the items table
        self.set_font('Helvetica', '', 10)
        self.cell(100, 10, 'Omschrijving', border=1)
        self.cell(30, 10, 'Aantal', border=1)
        self.cell(30, 10, 'Prijs', border=1)
        self.cell(30, 10, 'Totaal', border=1)
        self.ln()

        # Reset font for items
        self.set_font('Helvetica', '', 10)

        total_amount = 0
        for item in invoice_items.entries:
            description = item.description
            quantity = item.quantity
            price = item.unit_price
            line_total = quantity * price
            total_amount += line_total

            # Add item row
            self.cell(100, 10, description, border=1)
            self.cell(30, 10, str(quantity), border=1)
            self.cell(30, 10, f"{price:.2f} EUR", border=1)
            self.cell(30, 10, f"{line_total:.2f} EUR", border=1)
            self.ln()

        btw_amount = total_amount * 0.19
        total_incl_btw = total_amount + btw_amount

        # Total amount
        self.set_font('Helvetica', '', 10)
        self.cell(160, 10, 'Totaal excl BTW:', border=1)
        self.cell(30, 10, f"{total_amount:.2f} EUR", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(160, 10, '21% BTW:', border=1)
        self.cell(30, 10, f"{btw_amount:.2f} EUR", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(160, 10, 'Totaal incl. BTW:', border=1)
        self.cell(30, 10, f"{total_incl_btw:.2f} EUR", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)



class InvoicePDFTemplate(FPDF):
    def __init__(
            self,
            input_package: InvoiceTemplateInput = None,
            invoice_details: InvoiceDetails = None,
            company_details: CompanyDetails = None,
            invoice_items: InvoiceCostItems = None,
            orientation = "portrait", 
            unit = "mm", 
            format = "A4", 
            font_cache_dir = "DEPRECATED"
            ) -> None:
        super().__init__(orientation, unit, format, font_cache_dir)
        
        if input_package:
            self.create_invoice(
                input_package.invoice_details, 
                input_package.company_details, 
                input_package.invoice_items
                )
        elif all([invoice_details, company_details, invoice_items]):
            self.create_invoice(
                invoice_details, 
                company_details, 
                invoice_items)
        

    def header(self):
        # Bedrijfsnaam
        self.set_font('Helvetica', '', 12)
        self.image('resources\\logo\\logo_white.png', 10, 8, 33)  # Adjust the path and size as needed
        self.cell(0, 10, "Factuur",  new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(10)  # Lijnbreuk

    def footer(self):
        # Pagina-nummer
        self.set_y(-30)
        self.set_font('Helvetica', '', 8)
        self.multi_cell(0, 10, 
            "Te betalen binnen 30 dagen (voor DD-MM-YYYY) op rekeningnummer NL12BANK0123456789\n"
            "t.n.v. STUKADOORSBEDRIJF onder vermelding van klantnummer en factuurnummer.", 
            align='C'
        )
        self.cell(0, 10, f"Pagina {self.page_no()}", align="C")

    def create_invoice(
            self, 
            invoice_details: InvoiceDetails,
            company_details: CompanyDetails,
            invoice_items: InvoiceCostItems 
            ) -> None:
        self.add_page()
        self.add_invoice_details(invoice_details)
        self.add_company_details(company_details)
        self.add_invoice_items(invoice_items)

    def render(self, path: str) -> None:
        self.output(path)

    def add_invoice_details(self, invoice_details: InvoiceDetails):
        self.set_font('Helvetica', '', 10)
        self.cell(100, 10, f"Factuurnummer: {invoice_details.invoice_number}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(100, 10, f"Datum: {invoice_details.date}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(100, 10, f"Naam klant: {invoice_details.customer_name}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(100, 10, f"Adres klant: {invoice_details.customer_address}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(10)

    def add_company_details(self, company_details: CompanyDetails):
        self.set_font('Helvetica', 'B', 8)
        self.set_xy(140, 20)
        self.multi_cell(0, 8, 
            f"{company_details.name}\n"
            f"{company_details.address}\n"
            f"{company_details.postcode}, {company_details.city}\n"
            f"{company_details.phone}\n"
            f"{company_details.email}\n"
            f"{company_details.kvk_number}\n"
            f"{company_details.btw_number}\n"
            f"{company_details.iban}",
            align='L'
        )

    def add_invoice_items(self, invoice_items: InvoiceCostItems):
        self.set_xy(10, 100)
        # Header for the items table
        self.set_font('Helvetica', '', 10)
        self.cell(100, 10, 'Omschrijving', border=1)
        self.cell(30, 10, 'Aantal', border=1)
        self.cell(30, 10, 'Prijs', border=1)
        self.cell(30, 10, 'Totaal', border=1)
        self.ln()

        # Reset font for items
        self.set_font('Helvetica', '', 10)

        total_amount = 0
        for item in invoice_items.entries:
            description = item.description
            quantity = item.quantity
            price = item.unit_price
            line_total = quantity * price
            total_amount += line_total

            # Add item row
            self.cell(100, 10, description, border=1)
            self.cell(30, 10, str(quantity), border=1)
            self.cell(30, 10, f"{price:.2f} EUR", border=1)
            self.cell(30, 10, f"{line_total:.2f} EUR", border=1)
            self.ln()

        btw_amount = total_amount * 0.19
        total_incl_btw = total_amount + btw_amount

        # Total amount
        self.set_font('Helvetica', '', 10)
        self.cell(160, 10, 'Totaal excl BTW:', border=1)
        self.cell(30, 10, f"{total_amount:.2f} EUR", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(160, 10, '21% BTW:', border=1)
        self.cell(30, 10, f"{btw_amount:.2f} EUR", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(160, 10, 'Totaal incl. BTW:', border=1)
        self.cell(30, 10, f"{total_incl_btw:.2f} EUR", border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)




class InvoicePDFWithStyleInput(FPDF):
    def __init__(
            self,
            input_package: InvoiceTemplateInput = None,
            styling_settings: StyleSettingsInputPackage = None, 
            orientation = "portrait", 
            unit = "mm", 
            format = "A4", 
            font_cache_dir = "DEPRECATED"
            ) -> None:
        super().__init__(orientation, unit, format, font_cache_dir)
        self.input_package: Optional[InvoiceTemplateInput] = input_package
        self.styling_settings: Optional[StyleSettingsInputPackage] = styling_settings
        self.create_invoice()


    def create_invoice(self) -> None:
        self.add_page()
        self.add_invoice_details()
        self.add_company_details()


    def render(self, path: str) -> None:
        self.output(path)


    def header(self):
        # Bedrijfsnaam
        self.set_font(self.styling_settings.general.font, self.styling_settings.header.font_style, self.styling_settings.header.font_size)
        self.image('resources\\logo\\logo_white.png', 10, 8, 33)  # Adjust the path and size as needed
        self.cell(0, 10, "Factuur",  new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(10)  # Lijnbreuk


    def footer(self):
        # bereken deadline
        deadline_datum: datetime = datetime.today() + timedelta(days=30)
        datum_string: str = deadline_datum.strftime("%d-%m-%Y")

        bedrijf_naam: str = self.input_package.company_details.name
        iban: str = self.input_package.company_details.iban
        # Pagina-nummer
        self.set_y(-30)
        self.set_font(self.styling_settings.general.font, self.styling_settings.footer.font_style, self.styling_settings.footer.font_size)
        self.multi_cell(0, 10, 
            f"Te betalen binnen 30 dagen (voor {datum_string}) op rekeningnummer {iban}\n"
            f"t.n.v. {bedrijf_naam} onder vermelding van klantnummer en factuurnummer.", 
            align='C'
        )
        self.cell(0, 10, f"Pagina {self.page_no()}", align="C")


    def add_invoice_details(self):
        self.set_font(
            self.styling_settings.general.font, 
            self.styling_settings.invoice_details.font_style, 
            self.styling_settings.invoice_details.font_size
            )
        
        self.cell(
            self.styling_settings.invoice_details.cell_width, 
            self.styling_settings.invoice_details.cell_height, 
            f"Factuurnummer: {self.input_package.invoice_details.invoice_number}", 
            new_x=XPos.LMARGIN, 
            new_y=YPos.NEXT
            )
        self.cell(
            self.styling_settings.invoice_details.cell_width, 
            self.styling_settings.invoice_details.cell_height, 
            f"Datum: {self.input_package.invoice_details.date}", 
            new_x=XPos.LMARGIN, 
            new_y=YPos.NEXT
            )
        self.cell(
            self.styling_settings.invoice_details.cell_width, 
            self.styling_settings.invoice_details.cell_height, 
            f"Naam klant: {self.input_package.invoice_details.customer_name}", 
            new_x=XPos.LMARGIN, 
            new_y=YPos.NEXT
            )
        self.cell(
            self.styling_settings.invoice_details.cell_width, 
            self.styling_settings.invoice_details.cell_height, 
            f"Adres klant: {self.input_package.invoice_details.customer_address}", 
            new_x=XPos.LMARGIN, 
            new_y=YPos.NEXT
            )
        
        self.ln(10)


    def add_company_details(self):
        self.set_font(
            self.styling_settings.general.font, 
            self.styling_settings.company_details.font_style, 
            self.styling_settings.company_details.font_size
            )
        
        # self.set_xy(140, 20)
        self.set_xy(145, 27.5)

        self.multi_cell(
            self.styling_settings.company_details.cell_width,
            self.styling_settings.company_details.cell_height,
            f"{self.input_package.company_details.name}\n"
            f"{self.input_package.company_details.address}\n"
            f"{self.input_package.company_details.postcode}, {self.input_package.company_details.city}\n"
            f"{self.input_package.company_details.phone}\n"
            f"{self.input_package.company_details.email}\n"
            f"{self.input_package.company_details.kvk_number}\n"
            f"{self.input_package.company_details.btw_number}\n"
            f"{self.input_package.company_details.iban}",
            align='L'
        )


    def add_invoice_items(self):
        self.set_xy(10, 100)
        # Header for the items table
        self.set_font(self.styling_settings.general.font, self.styling_settings.invoice_items.font_style, self.styling_settings.invoice_items.font_size)

        self.cell(100, 10, 'Omschrijving', border=self.styling_settings.table.border)
        self.cell(30, 10, 'Aantal', border=self.styling_settings.table.border)
        self.cell(30, 10, 'Prijs', border=self.styling_settings.table.border)
        self.cell(30, 10, 'Totaal', border=self.styling_settings.table.border)
        self.ln()

        # Reset font for items
        self.set_font(self.styling_settings.general.font, self.styling_settings.invoice_items.font_style, self.styling_settings.invoice_items.font_size)

        total_amount = 0
        for item in self.input_package.invoice_items.entries:
            description = item.description
            quantity = item.quantity
            price = item.unit_price
            line_total = quantity * price
            total_amount += line_total

            # Add item row
            self.cell(100, 10, description, border=self.styling_settings.table.border)
            self.cell(30, 10, str(quantity), border=self.styling_settings.table.border)
            self.cell(30, 10, f"{price:.2f} EUR", border=self.styling_settings.table.border)
            self.cell(30, 10, f"{line_total:.2f} EUR", border=self.styling_settings.table.border)
            self.ln()

        btw_amount = total_amount * self.input_package.invoice_details.calculation_info.btw_percentage
        total_incl_btw = total_amount + btw_amount

        # Total amount
        self.set_font('Helvetica', '', 10)
        self.cell(160, 10, 'Totaal excl BTW:', border=self.styling_settings.table.border)
        self.cell(30, 10, f"{total_amount:.2f} EUR", border=self.styling_settings.table.border, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(160, 10, '21% BTW:', border=self.styling_settings.table.border)
        self.cell(30, 10, f"{btw_amount:.2f} EUR", border=self.styling_settings.table.border, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(160, 10, 'Totaal incl. BTW:', border=self.styling_settings.table.border)
        self.cell(30, 10, f"{total_incl_btw:.2f} EUR", border=self.styling_settings.table.border, new_x=XPos.LMARGIN, new_y=YPos.NEXT)