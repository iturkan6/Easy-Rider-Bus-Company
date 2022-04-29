import json


def take_info():
    lines = {}
    for dictionary in data:
        v = dictionary["bus_id"]
        if v not in lines.keys():
            lines[v] = 1
        else:
            lines[v] += 1
    print("Line names and number of stops:")
    [print("bus_id: ", k, ", ", "stops: ", v, sep="") for k, v in lines.items()]


if __name__ == "__main__":
    data = json.loads(input())
    take_info()
