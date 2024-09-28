#!/usr/bin/python
from  .. import day
from typing import Generator

"""
Year 2015 - Day 2 : I Was Told There Would Be No Math
Solves the December 2nd 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_02
"""
    
def parse_data(input_data) -> Generator[list[int], None, None]:
    input_data = input_data.splitline()
    for data in input_data:
        yield sorted(list(map(int, data.split("x"))))

def part_one(input_data: str):
    return sum(2 * (l*w + l*h + w*h) + min(l*w, l*h, w*h) for l, w, h in parse_data(input_data))

def part_two(input_data: str):
    return sum(2 * l + 2 * w + l * w * h for l, w, h in parse_data(input_data))

def main():
    pod = day.PuzzleOfTheDay(2015, 2)
    pod.submit("a", part_one(pod.input_data))
    pod.submit("b", part_two(pod.input_data))


if __name__ == "__main__":
    main()
