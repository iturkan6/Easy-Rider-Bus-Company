import json
import time


def take_info() -> None:
    for i in range(len(data) - 1):
        cur_bus = data[i]
        next_bus = data[i + 1]
        bus_id = cur_bus["bus_id"]
        cur_time = time.strptime(cur_bus["a_time"], "%H:%M")
        next_time = time.strptime(next_bus["a_time"], "%H:%M")
        if cur_time > next_time and bus_id == next_bus["bus_id"] and bus_id not in lines:
            lines[bus_id] = next_bus["stop_name"]
    print("Arrival time test:")
    if lines:
        [print("bus_id line ", k, ": wrong time on station ", v, sep="") for k, v in lines.items()]
    else:
        print("OK")


if __name__ == "__main__":
    lines = {}
    data = json.loads(input())
    take_info()
