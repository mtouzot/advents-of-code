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


def main():
    pod = day.PuzzleOfTheDay(2015, 1)
    first_time_in_basement = None
    for idx, floor in enumerate(count_floors(pod.input_data)):
        if floor == -1 and first_time_in_basement is None:
            first_time_in_basement = idx + 1
    pod.submit("a", floor)
    pod.submit("b", first_time_in_basement)


if __name__ == "__main__":
    main()
