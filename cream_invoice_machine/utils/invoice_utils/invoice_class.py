"""
Sctipt containing the invoice class. 

This class is responsible for and implements the structure of 
the generated pdf pages.
"""
import os
from fpdf import FPDF, XPos, YPos

from typing import List

from cream_invoice_machine.templates.pdf import InvoiceHeaderTemplate
from cream_invoice_machine.utils.invoice_utils.invoice_dataclasses import InvoiceDetails, InvoiceLineItems, CompDetails




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

    def add_company_details(self, company_details: CompDetails):
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

    def add_invoice_items(self, invoice_items: InvoiceLineItems):
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


class TESTInvoicePDF(FPDF):
    def __init__(self, orientation='P', unit='mm', format='A4'):
        super().__init__(orientation, unit, format)
        self.add_fonts()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        self.set_margins(10, 10, 10)

    def add_fonts(self):
        # Voeg aangepaste lettertypen toe als dat nodig is
        self.add_font('DejaVu', '', os.path.abspath(os.path.join('resources', 'fonts', 'DejaVuSansCondensed.ttf')), uni=True)
        self.add_font('DejaVu', 'B', os.path.abspath(os.path.join('resources', 'fonts', 'DejaVuSans-Bold.ttf')), uni=True)
        self.add_font('DejaVu', 'I', os.path.abspath(os.path.join('resources', 'fonts', 'DejaVuSans-Oblique.ttf')), uni=True)

    def header(self):
        # Voeg een logo toe
        self.image('resources\\logo\\logo_white.png', 10, 8, 33)
        self.set_font('DejaVu', 'B', 12)
        self.cell(0, 10, 'Factuur', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-35)
        self.multi_cell(0, 10, 
            "Te betalen binnen 30 dagen (voor DD-MM-YYYY) op rekeningnummer NL12BANK0123456789\n"
            "t.n.v. STUKADOORSBEDRIJF onder vermelding van klantnummer en factuurnummer.", 
            align='C'
        )
        self.set_font('DejaVu', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}', 0, 0, 'C')

    def add_client_info(self, client_name, client_address):
        self.set_font('DejaVu', '', 10)
        self.cell(0, 10, f'Klantnaam: {client_name}', 0, 1)
        self.cell(0, 10, f'Adres: {client_address}', 0, 1)
        self.ln(10)

    def add_invoice_table(self, items: InvoiceLineItems):
        self.set_font('DejaVu', 'B', 10)
        self.set_fill_color(200, 220, 255)
        self.cell(40, 10, 'Omschrijving', 1, 0, 'C', 1)
        self.cell(30, 10, 'Aantal', 1, 0, 'C', 1)
        self.cell(30, 10, 'Prijs per stuk', 1, 0, 'C', 1)
        self.cell(30, 10, 'Totaal', 1, 1, 'C', 1)
        self.set_font('DejaVu', '', 10)
        self.set_fill_color(245, 245, 245)
        fill = False
        for item in items.items:
            self.cell(40, 10, item.description, 1, 0, 'L', fill)
            self.cell(30, 10, str(item.quantity), 1, 0, 'C', fill)
            self.cell(30, 10, str(item.unit_price), 1, 0, 'R', fill)
            self.cell(30, 10, str(item.total), 1, 1, 'R', fill)
            fill = not fill

    def add_total_amount(self, total):
        self.set_font('DejaVu', 'B', 10)
        self.cell(100, 10, '', 0, 0)
        self.cell(30, 10, 'Totaalbedrag:', 0, 0, 'R')
        self.cell(30, 10, f"€ {total:.2f}", 1, 1, 'R')