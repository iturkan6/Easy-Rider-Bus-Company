import json


def take_info() -> None:
    for i in range(len(data)):
        cur = data[i]
        bus_id = str(cur["bus_id"])
        if not check(bus_id, cur["stop_type"], cur["stop_name"], cur["next_stop"]):
            return None
    transfer_result = sorted([k for k, v in transfer.items() if v > 1])
    print("Start stops: {} {}".format(len(start), sorted(start)))
    print("Transfer stops: {} {}".format(len(transfer_result), transfer_result))
    print("Finish stops: {} {}".format(len(finish), sorted(finish)))


def check(bus_id, stop_type, stop_name, next_stop) -> bool:
    if bus_id not in lines:
        lines[bus_id] = set()

    count = len(lines[bus_id])

    if count == 0 and stop_type == "S":
        start.add(stop_name)
    elif next_stop == 0 and stop_type == "F":
        finish.add(stop_name)
    elif count == 0 and stop_type != "S" or next_stop == 0 and stop_type != "F":
        print(f"There is no start or end stop for the line: {bus_id}.")
        return False
    if stop_name not in transfer:
        transfer[stop_name] = 0
    transfer[stop_name] += 1
    lines[bus_id].add(stop_name)
    return True


if __name__ == "__main__":
    transfer = {}
    lines = {}
    start = set()
    finish = set()
    data = json.loads(input())
    take_info()
