import json


def task() -> float:
    file_path = "input.json"
    with open(file_path) as f:
        start_data = json.load(f)
        total_sum = 0
        for i in start_data:
            total_sum += i['weight'] * i['score']
    return round(total_sum, 3)


data = task()
print(data)
