#!/usr/bin/python
from  .. import day
from string import ascii_lowercase
import re

"""
Year 2015 - Day 11 : Corporate Policy
Solves the December 11th 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_11
"""

    
def increment_pwd(input_data: str,
                  idx: int = -1):
    pwd = list(input_data)
    current_ord = ord(pwd[idx])
    if current_ord == ord('z'):
        pwd[idx] = 'a'
        input_data = ''.join(pwd)
        input_data = increment_pwd(input_data, idx-1)
    else:
        pwd[idx] = chr(current_ord + 1)
        input_data = ''.join(pwd)
    return input_data

def straight_increasing(input_data: str,
                        n: int = 3):
    for idx in range(len(input_data) - n + 1):
        if (input_data[idx:idx+n] in ascii_lowercase):
            return True
    return False

def contains_iol(input_data: str):
    return len(re.findall(r"[iol]", input_data)) > 0

def at_least_n_non_overlapping_pairs(input_data: str,
                                     n: int = 1) -> bool:
    pairs = re.findall(r"(.)\1", input_data)
    return len(pairs) >= n

def is_valid(input_data) -> bool:
    return len(input_data) == 8 and at_least_n_non_overlapping_pairs(input_data, 2) and straight_increasing(input_data) and not contains_iol(input_data)

def part_one(input_data) -> str:
    while not is_valid(input_data):
        input_data = increment_pwd(input_data)
    return input_data

def part_two(input_data) -> str:
    return part_one(increment_pwd(part_one(input_data)))

if __name__ == "__main__":
    pod = day.PuzzleOfTheDay(2015, 11)
    pod.submit("a", part_one(pod.input_data))
    pod.submit("b", part_two(pod.input_data))
