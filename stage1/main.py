import json


def take_info():
    errors = {"bus_id": 0, "stop_id": 0, "stop_name": 0, "next_stop": 0, "stop_type": 0, "a_time": 0}
    stop_types = ("S", "O", "F")
    for dict_ in data:
        if type(dict_["bus_id"]) is not int:
            errors["bus_id"] += 1
        if type(dict_["stop_id"]) is not int:
            errors["stop_id"] += 1
        if type(dict_["stop_name"]) is not str or not dict_["stop_name"]:
            errors["stop_name"] += 1
        if type(dict_["next_stop"]) is not int:
            errors["next_stop"] += 1
        if dict_["stop_type"] not in stop_types and dict_["stop_type"] != "":
            errors["stop_type"] += 1
        if type(dict_["a_time"]) is not str or not dict_["a_time"]:
            errors["a_time"] += 1
    print("""Type and required field validation: {} errors
    bus_id: {}
    stop_id: {}
    stop_name: {}
    next_stop: {}
    stop_type: {}
    a_time: {}""".format(sum(errors.values()), *errors.values()))


if __name__ == "__main__":
    s = input()
    data = json.loads(s)
    take_info()
