import json


def take_info():
    errors = {"bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0, "stop_type": 0, "a_time": 0}
    for dictionary in data:
        for k, v in dictionary.items():
            if not validator[k](v):
                errors[k] += 1
    print(f"Type and required field validation: {sum(errors.values())} errors")
    [print(k, ": ", v, sep="") for k, v in errors.items()]


def dict_data(dictionary: dict, key: str):
    return type(dictionary[key])


if __name__ == "__main__":
    stop_types = ("S", "O", "F")
    validator = {
        "bus_id": lambda info: type(info) is int,
        "stop_id": lambda info: type(info) is int,
        "stop_name": lambda info: type(info) is str and info,
        "next_stop": lambda info: type(info) is int,
        "stop_type": lambda info: info in stop_types or not info,
        "a_time": lambda info: type(info) is str and info,
    }
    data = json.loads(input())
    take_info()
