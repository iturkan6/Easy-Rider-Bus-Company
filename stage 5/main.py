import json
import time


def take_info() -> None:
    for i in range(len(data) - 1):
        cur_bus = data[i]
        next_bus = data[i + 1]
        bus_id = cur_bus["bus_id"]
        if conv_time(cur_bus) > conv_time(next_bus) and bus_id == next_bus["bus_id"] and bus_id not in lines:
            lines[bus_id] = next_bus["stop_name"]
    print("Arrival time test:")
    if lines:
        [print("bus_id line ", k, ": wrong time on station ", v, sep="") for k, v in lines.items()]
    else:
        print("OK")


def conv_time(bus):
    return time.strptime(bus["a_time"], "%H:%M")


if __name__ == "__main__":
    lines = {}
    data = json.loads(input())
    take_info()
