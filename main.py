import json


def take_info():
    errors = {"bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0, "stop_type": 0, "a_time": 0}
    stop_types = ("S", "O", "F")
    for dictionary in data:
        if dict_data(dictionary, "bus_id") is not int:
            errors["bus_id"] += 1
        if type(dictionary["stop_id"]) is not int:
            errors["stop_id"] += 1
        if type(dictionary["stop_name"]) is not str or not dictionary["stop_name"]:
            errors["stop_name"] += 1
        if type(dictionary["next_stop"]) is not int:
            errors["next_stop"] += 1
        if dictionary["stop_type"] not in stop_types and dictionary["stop_type"] != "":
            errors["stop_type"] += 1
        if type(dictionary["a_time"]) is not str or not dictionary["a_time"]:
            errors["a_time"] += 1
    print("""Type and required field validation: {} errors
bus_id: {}
stop_id: {}
stop_name: {}
next_stop: {}
stop_type: {}
a_time: {}""".format(sum(errors.values()), *errors.values()))


def dict_data(dictionary: dict, key: str):
    return type(dictionary[key])


if __name__ == "__main__":
    s = input()
    data = json.loads(s)
    take_info()
