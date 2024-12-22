"""
Scripts to orchestrate reading and preparing the input variables.

This includes the input .yaml-files
"""
import os
from datetime import datetime

import dotenv

from cream_invoice_machine.utils.file_reader import read_yaml, read_env_variable

dotenv.load_dotenv('.env')


class CorpInforManager:

    _file_path: str = read_env_variable("CORP_INFO_PATH")

    def __init__(self):
        print(self._file_path)

