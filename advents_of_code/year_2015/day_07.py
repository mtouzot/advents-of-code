#!/usr/bin/python
from .. import day
from typing import Union
from functools import cache
from operator import and_, or_, lshift, rshift

"""
Year 2015 - Day 7 : Some Assembly Required
Solves the December 7th 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_07
"""

def parse_data(input_data: list[str]) -> dict:
    wires = {}
    for data in input_data:
        *expression, _, wire = data.split()
        wires[wire] = expression
    return wires

@cache
def compute_signal(wire_output: str):
    global wires
    operations = dict(AND=and_,
                        OR=or_,
                        LSHIFT=lshift,
                        RSHIFT=rshift)
    if wire_output.isnumeric():
        return int(wire_output)
    match wires[wire_output]:
        case [output]:
            return compute_signal(output)
        case ["NOT", output]:
            return ~compute_signal(output)
        case [a, operation, b]:
            return operations[operation](compute_signal(a),
                                         compute_signal(b))

def part_one():
    global wires
    return compute_signal("a")

def part_two():
    global wires
    wires["b"] = [str(part_one())]
    compute_signal.cache_clear()
    return compute_signal("a")


if __name__ == "__main__":
    pod = day.PuzzleOfTheDay(2015, 7)
    wires = parse_data(pod.input_data.split("\n"))
    pod.submit("a", part_one())
    pod.submit("b", part_two())