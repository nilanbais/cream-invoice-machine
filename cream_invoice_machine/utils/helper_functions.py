from typing import List

def flatten_list_of_dicts(input_list: List[dict]) -> dict:
    result: dict = {}
    for item in input_list:
        result.update(item)
    return result