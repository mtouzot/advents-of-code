#!/usr/bin/python
import re
import json
from  .. import day

"""
Year 2015 - Day 12 : JSAbacusFramework.io
Solves the December 12th 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_12
"""


def extract_numbers(input_data: str):
    numbers = re.findall(r"-*\d+", input_data)
    return [int(nbr) for nbr in numbers]

def count(account):
    if (isinstance(account, dict)\
        and "red" in account.values())\
            or isinstance(account, str):
        return 0
    elif isinstance(account, dict):
        return sum(map(count, account.values()))
    elif isinstance(account, list):
        return sum(map(count, account))
    else:
        return account

def part_one(input_data: str) -> int:
    return sum(extract_numbers(input_data))

def part_two(input_data):
    data = json.loads(input_data)
    return count(data)

if __name__ == "__main__":
    pod = day.PuzzleOfTheDay(2015, 12)
    pod.submit("a", part_one(pod.input_data))
    pod.submit("b", part_two(pod.input_data))
