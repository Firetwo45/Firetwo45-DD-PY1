import json

INPUT_FILE = "input_1.csv"


def csv_to_list_dict(export) -> list[dict]:
    with open(export, 'r') as f:
        values = []
        for line in f:
            words = line.rstrip("\n").split(',')
            values.append(words)
        values = values[::2]
        headers = values[0]
        values = values[1:]

        result = []
        for vals in values:
            # print(vals)
            vals = [format(float(val), '.6f') for val in vals]
            result.append(dict(zip(headers, vals)))
        # print(result)
        return result


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
