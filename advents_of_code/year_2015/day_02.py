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
    input_data = input_data.split("\n")
    for data in input_data:
        yield sorted(list(map(int, data.split("x"))))

def main():
    pod = day.PuzzleOfTheDay(2015, 2)
    first_rule_area = 0
    second_rule_area = 0
    for [l, w, h] in parse_data(pod.input_data):
        area = [l*w, l*h, w*h]
        first_rule_area += 2 * sum(area) + min(area)
        second_rule_area += 2 * l + 2 * w + l * w * h
    pod.submit("a", first_rule_area)
    pod.submit("b", second_rule_area)


if __name__ == "__main__":
    main()
