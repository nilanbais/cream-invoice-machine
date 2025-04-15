import os
from datetime import datetime

from typing import List, Optional

from cream_invoice_machine.utils.file_readers import read_env_variable
from cream_invoice_machine.models.dataclasses import (
    InvoiceLineItem, 
    InvoiceCostItems,
    StyleSettings
    )


def list_files(path: str) -> list:
    folder_content: list = os.listdir(path)
    # change folder_content to contain full path
    folder_content: list = [os.path.join(path, item) for item in folder_content]
    # filter directories from folder content
    folder_content: list = [item for item in folder_content if not os.path.isdir(item)]
    
    return folder_content

def basename_from_path(path: str) -> str:
    normpath = os.path.normpath(path)
    return os.path.basename(normpath)


def style_settings_from_dict(input_dict: Optional[dict] = None) -> StyleSettings:
    raw_dict: dict = {} if input_dict is None else input_dict

    reference_list: list = [
        "font", 
        "font-size", 
        "font-style",
        "cell-width",
        "cell-height",        
        "border"
        ]
    
    missing_items: list = [item for item in reference_list if item not in input_dict.keys()]
    
    for item in missing_items:
        raw_dict[item] = None

    style_settings: StyleSettings = StyleSettings(
        font=raw_dict['font'],
        font_size=raw_dict['font-size'],
        font_style=raw_dict['font-style'],
        cell_width=raw_dict['cell-width'],
        cell_height=raw_dict['cell-height'],
        border=raw_dict['border']
    )

    return style_settings


def flatten_list_of_dicts(input_list: List[dict]) -> dict:
    result: dict = {}
    for item in input_list:
        result.update(item)
    return result


def flatten_nested_dict(input_dict: dict) -> dict:
    result: dict = {}
    for key, value in input_dict.items():
        if isinstance(value, dict):
            for nested_key, nested_value in value.items():
                new_key = str().join([key, ' - ', nested_key])
                result[new_key] = nested_value
        else:
            result[key] = value
    return result


def invoice_items_from_list(input_list: List[dict]) -> InvoiceCostItems:

    # Convert dictionaries to InvoiceItem instances
    invoice_items: List[InvoiceLineItem] = [InvoiceLineItem(**item) for item in input_list]
    return InvoiceCostItems(entries=invoice_items)
