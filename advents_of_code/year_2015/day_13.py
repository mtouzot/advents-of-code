#!/usr/bin/python
from itertools import permutations, islice, tee
from  .. import day

"""
Year 2015 - Day 13 : Knights of Dinner Table
Solves the December 13th 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_13
"""


def parse_data(input_data: list[str]):
    dinner_tables = dict()
    coeff = {"gain": 1, "lose": -1}
    for data in input_data:
        person_A, _, sign, units, *_, person_B = data[:-1].split()
        dinner_tables.setdefault(person_A, {})[person_B] = coeff[sign] * int(units)
    return dinner_tables

def compute_happiness(input_data: dict) -> list[int]:
    sum_happiness = []
    for p in permutations(input_data):
        happiness = 0
        p = (*p, p[0])
        for start, end in zip(tee(p)[0], islice(tee(p)[1], 1, None)):
            happiness += input_data[start][end] + input_data[end][start]
        sum_happiness.append(happiness)
    return sum_happiness

def part_one(input_data: dict) -> int:
    return max(compute_happiness(input_data))

def part_two(input_data: dict) -> None:
    table_with_santa = dict()
    for personn in input_data.keys():
        table_with_santa.setdefault("santa", {})[personn] = 0
        input_data[personn].update({"santa": 0})
    input_data |= table_with_santa
    return max(compute_happiness(input_data))

if __name__ == "__main__":
    pod = day.PuzzleOfTheDay(2015, 13)
    input_data = parse_data(pod.input_data.splitlines())
    pod.submit("a", part_one(input_data))
    pod.submit("b", part_two(input_data))
