#!/usr/bin/python
from  .. import day
from typing import Generator

"""
Year 2015 - Day 1 : Not Quite Lisp
Solves the December 1st 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_01
"""

def count_floors(input_data: str) -> Generator[int, None, None]:
    direction = {'(': 1, ')': -1}
    current_floor = 0
    for char in input_data:
        current_floor += direction[char]
        yield current_floor

def part_one(input_data: str):
    *_, last = count_floors(input_data)
    return last

def part_two(input_data: str):
    return list(count_floors(input_data)).index(-1) + 1

def main():
    pod = day.PuzzleOfTheDay(2015, 1)
    pod.submit("a", part_one(pod.input_data))
    pod.submit("b", part_two(pod.input_data))


if __name__ == "__main__":
    main()
