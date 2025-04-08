
from fpdf import FPDF, FlexTemplate

from typing import List



class InvoiceHeaderTemplate:

    elements: List[dict] = [
        {
            "name": "logo", "type": "I", "x1": 10, "y1": 8, "x2": 30, "y2": 20, "file": "cream-invoice-machine\\resources\\logo\\logo_white.png"
        },
        {
            "name": "title", "type": "T", "x1": 40, "y1": 10, "x2": 200, "y2": 20, "font": "helvetica", "size": 12, "align": "L", "text": ""
        },
        {
            "name": "adres", "type": "T", "x1": 40, "y1": 20, "x2": 200, "y2": 300, "font": "helvetica", "size": 12, "align": "L", "text": ""
        },
    ]

    def __init__(self, pdf_object: FPDF) -> None:
        self._flex_template = FlexTemplate(pdf_object, elements=self.elements)

    @property
    def title(self) -> str:
        return
    
    @title.setter
    def title(self, value) -> None:
        self._flex_template["title"] = value

    @property
    def adres(self) -> None:
        return
    
    @adres.setter
    def adres(self, value) -> None:
        self._flex_template["adres"] = value

    def render(self) -> None:
        self._flex_template.render()