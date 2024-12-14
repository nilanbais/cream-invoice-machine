import os
from fpdf import FPDF

class InvoicePDF(FPDF):
    def __init__(self, orientation = "portrait", unit = "mm", format = "A4", font_cache_dir = "DEPRECATED"):
        super().__init__(orientation, unit, format, font_cache_dir)

        # font_path = os.path.join(os.path.dirname(__file__), "DejaVuSans.ttf")
        # self.add_font("DejaVu", style="", fname=font_path, uni=True)

    def header(self):
        # Bedrijfsnaam
        self.set_font("DejaVu", "", 12)
        self.cell(0, 10, "Bedrijf XYZ", ln=True, align="C")
        self.set_font("DejaVu", "", 10)
        self.cell(0, 10, "Adres: Straat 123, 4567 AB Plaatsnaam", ln=True, align="C")
        self.ln(10)  # Lijnbreuk

    def footer(self):
        # Pagina-nummer
        self.set_y(-15)
        self.set_font("DejaVu", "", 8)
        self.cell(0, 10, f"Pagina {self.page_no()}", align="C")

    def add_invoice_details(self, invoice_number, date, customer_name, customer_address):
        self.set_font("DejaVu", "", 10)
        self.cell(100, 10, f"Factuurnummer: {invoice_number}")
        self.cell(0, 10, f"Datum: {date}", ln=True)
        self.cell(100, 10, f"Naam klant: {customer_name}")
        self.cell(0, 10, f"Adres klant: {customer_address}", ln=True)
        self.ln(10)

    def add_table(self, items):
        # Tabel kop
        self.set_font("DejaVu", "", 10)
        self.cell(80, 10, "Artikel", border=1, align="C")
        self.cell(30, 10, "Aantal", border=1, align="C")
        self.cell(40, 10, "Prijs per stuk", border=1, align="C")
        self.cell(40, 10, "Totaal", border=1, align="C")
        self.ln()

        # Dynamische rijen
        self.set_font("DejaVu", "", 10)
        total_price = 0
        for item in items:
            article, quantity, unit_price = item
            line_total = quantity * unit_price
            total_price += line_total
            self.cell(80, 10, article, border=1)
            self.cell(30, 10, str(quantity), border=1, align="C")
            self.cell(40, 10, f"€ {unit_price:.2f}", border=1, align="R")
            self.cell(40, 10, f"€ {line_total:.2f}", border=1, align="R")
            self.ln()

        # Totaalbedrag
        self.set_font("DejaVu", "", 10)
        self.cell(150, 10, "Totaal", border=1, align="R")
        self.cell(40, 10, f"€ {total_price:.2f}", border=1, align="R")