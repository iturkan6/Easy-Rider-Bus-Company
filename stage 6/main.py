import json
from time import strptime


def take_info() -> None:
    for i in range(len(data)):
        cur_bus = data[i]
        stop_type = cur_bus["stop_type"]
        stop_name = cur_bus["stop_name"]
        if stop_type in "SF":
            start_finish.add(stop_name)
        if stop_type == "O":
            on_demand.add(stop_name)
    result = start_finish & on_demand
    print("On demand stops test:")
    print(f"Wrong stop type: {sorted(result)}" if result else "OK")


if __name__ == "__main__":
    start_finish = set()
    on_demand = set()
    data = json.loads(input())
    take_info()
