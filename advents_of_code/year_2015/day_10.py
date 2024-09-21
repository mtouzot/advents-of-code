#!/usr/bin/python
from functools import cache
from  .. import day

"""
Year 2015 - Day 10 : Elves Look, Elves Say
Solves the December 10th 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_10
"""


def look_and_say(input_data: str,
                 n: int = 1) -> str:
    if n == 1:
        input_data = input_data
    else:
        input_data = look_and_say(input_data, n-1)
    res = ''
    count = 0
    prev_number = input_data[0]
    for number in input_data:
        if number == prev_number:
            count += 1
        else:
            res += f"{count}{prev_number}"
            count = 1
            prev_number = number
    res += f"{count}{prev_number}"
    return res

if __name__ == "__main__":
    pod = day.PuzzleOfTheDay(2015, 10)
    pod.submit("a", len(look_and_say(pod.input_data, 40)))
    pod.submit("b", len(look_and_say(pod.input_data, 50)))
