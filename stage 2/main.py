import json
import re


def take_info():
    errors = {"stop_name": 0, "stop_type": 0, "a_time": 0}
    for dictionary in data:
        for k, v in dictionary.items():
            if k in errors.keys() and not validator[k](v):
                errors[k] += 1
    print(f"Type and required field validation: {sum(errors.values())} errors")
    [print(k, ": ", v, sep="") for k, v in errors.items()]


def dict_data(dictionary: dict, key: str):
    return type(dictionary[key])


if __name__ == "__main__":
    stop_types = ("S", "O", "F", "")
    validator = {
        "stop_name": lambda info: re.match(r"([A-Z][a-z]* )+(Road|Avenue|Boulevard|Street)$", info),
        "stop_type": lambda info: info in stop_types,
        "a_time": lambda info: re.match(r"(0[0-9]|1[0-9]|2[0-3]):(0[0-9]|[1-5][0-9])$", info),
    }
    data = json.loads(input())
    take_info()