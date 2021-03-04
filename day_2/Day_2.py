from collections import Counter
from typing import List


def is_between(value, mini, maxi):
    return not (value < mini or value > maxi)


def read_data(filepath) -> List:
    data = []
    with open(filepath, "r") as file:
        lines = file.readlines()
    for line in lines:
        line_split = line.split()
        counts = line_split[0]
        letter = line_split[1][0]
        password = line_split[2]
        counts_split = counts.split("-")
        min_occu = int(counts_split[0])
        max_occu = int(counts_split[1])
        line_json = {
            "letter": letter,
            "min_occu": min_occu,
            "max_occu": max_occu,
            "password": password
        }
        data.append(line_json)
    return data


def count_valid_pass_part_1(entries) -> int:
    count_valid = 0
    for entrie in entries:
        letter = entrie["letter"]
        password = entrie["password"]
        min_occu = entrie["min_occu"]
        max_occu = entrie["max_occu"]
        counts = Counter(password)
        counts_letter = counts[letter]
        if is_between(counts_letter, min_occu, max_occu):
            count_valid += 1
    return count_valid


def count_valid_pass_part_2(entries):
    count_valid = 0
    for entrie in entries:
        letter = entrie["letter"]
        password = entrie["password"]
        min_occu = entrie["min_occu"]-1
        max_occu = entrie["max_occu"]-1
        if min_occu < len(password) and max_occu < len(password):
            if (password[min_occu] == letter) ^ (password[max_occu] == letter):
                count_valid += 1
                print(entrie)
    return count_valid


# print(is_between(101,5,100))

data = read_data("./data/data_1.txt")
valids = count_valid_pass_part_1(data)
print("Answer part 1: " + str(valids))

data = read_data("./data/data_2.txt")
valids = count_valid_pass_part_2(data)
print("Answer part 2: " + str(valids))
