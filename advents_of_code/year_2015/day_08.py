#!/usr/bin/python
from  .. import day

"""
Year 2015 - Day 8 : Matchsticks
Solves the December 8th 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_08
"""


def part_one(input_data) -> int:
    return sum(len(data) - len(eval(data)) for data in input_data)

def part_two(input_data) -> int:
    return sum(2 + data.count("\"") + data.count("\\") for data in input_data)

if __name__ == "__main__":
    pod = day.PuzzleOfTheDay(2015, 8)
    input_data = pod.input_data.splitlines()
    pod.submit("a", part_one(input_data))
    pod.submit("b", part_two(input_data))
