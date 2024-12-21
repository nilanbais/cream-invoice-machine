"""
Script/functionalities to handle reading data from files.
"""
import os
import yaml

def read_yaml(path: str) -> dict:
    """Reads .yaml-file and returns a py-dict"""
    abs_path: str = os.path.abspath(path)
    with open(abs_path) as yaml_file:
        try:
            file_content = yaml.safe_load(yaml_file)
        except yaml.YAMLError as exception:
            print(exception)

    return file_content