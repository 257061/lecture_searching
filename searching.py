import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    import json

    with open("sequential.json", mode="r") as data_file:
        data = json.load(data_file)
    for key in data_keys():
        if field == key:
            sequential_data = data[field]
            return sequential_data
        else:
            return None


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print("Sequential Data:", sequential_data)


def linear_search(sequence, target):

    positions = []
    count = 0
    for i, num in enumerate(sequence):
         if num == target:
            positions.append(i)
            count += 1

    return {"positions": positions, "count": count}


def pattern_search(sequence, pattern):

    positions = set()
    seq_length = len(sequence)
    pattern_length = len(patterm)

    for i in range(seq_length - pattern_length + 1):
        if sequence[i:i + pattern_length] == pattern:
            positions.add((i + pattern_length)/2)

    return positions



if __name__ == '__main__':
    main()