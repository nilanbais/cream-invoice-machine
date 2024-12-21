"""
Sctipt containing the invoice class. 

This class is responsible for and implements the structure of 
the generated pdf pages.
"""
from fpdf import FPDF, XPos, YPos

from typing import List

from cream_invoice_machine.templates.pdf import InvoiceHeaderTemplate
from cream_invoice_machine.utils.invoice_utils.invoice_dataclasses import InvoiceDetails, InvoiceItems







class InvoicePDF(FPDF):
    def __init__(self, orientation = "portrait", unit = "mm", format = "A4", font_cache_dir = "DEPRECATED"):
        super().__init__(orientation, unit, format, font_cache_dir)

    def header(self):
        # Bedrijfsnaam
        self.set_font("DejaVu", "", 12)
        self.image('C:\\Users\\NilanBais\\Documents\\Github\\cream-invoice-machine\\resources\\logo\\logo_white.png', 10, 8, 33)  # Adjust the path and size as needed
        self.cell(0, 10, "Bedrijf XYZ",  new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.set_font("DejaVu", "", 10)
        self.cell(0, 10, "Adres: Straat 123, 4567 AB Plaatsnaam", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(10)  # Lijnbreuk

    def footer(self):
        # Pagina-nummer
        self.set_y(-30)
        self.set_font("DejaVu", "", 8)
        self.multi_cell(0, 10, 
            "Te betalen binnen 30 dagen (voor DD-MM-YYYY) op rekeningnummer NL12BANK0123456789\n"
            "t.n.v. STUKADOORSBEDRIJF onder vermelding van klantnummer en factuurnummer.", 
            align='C'
        )
        self.cell(0, 10, f"Pagina {self.page_no()}", align="C")

    def add_invoice_details(self, invoice_details: InvoiceDetails):
        self.set_font("DejaVu", "", 10)
        self.cell(100, 10, f"Factuurnummer: {invoice_details.invoice_number}")
        self.cell(100, 10, f"Datum: {invoice_details.date}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.cell(100, 10, f"Naam klant: {invoice_details.customer_name}")
        self.cell(100, 10, f"Adres klant: {invoice_details.customer_address}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(10)

    def add_invoice_items(self, invoice_items: InvoiceItems):
        # Header for the items table
        self.set_font("DejaVu", "", 10)
        self.cell(100, 10, 'Omschrijving', border=1)
        self.cell(30, 10, 'Aantal', border=1)
        self.cell(30, 10, 'Prijs', border=1)
        self.cell(30, 10, 'Totaal', border=1)
        self.ln()

        # Reset font for items
        self.set_font('Helvetica', '', 10)

        total_amount = 0
        for item in invoice_items.items:
            description = item.description
            quantity = item.quantity
            price = item.price
            line_total = quantity * price
            total_amount += line_total

            # Add item row
            self.cell(100, 10, description, border=1)
            self.cell(30, 10, str(quantity), border=1)
            self.cell(30, 10, f"{price:.2f} EUR", border=1)
            self.cell(30, 10, f"{line_total:.2f} EUR", border=1)
            self.ln()

        # Total amount
        self.set_font("DejaVu", "", 10)
        self.cell(160, 10, 'Totaal:', border=1)
        self.cell(30, 10, f"€ {total_amount:.2f}", border=1)