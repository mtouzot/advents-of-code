#!/usr/bin/python
from  .. import day
from itertools import combinations

"""
Year 2015 - Day 17: No Such Thing as Too Much
Solves the December 17th 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_17
"""


def get_all_size_combinations(input_data: list[int],
                              max_size: int) -> list[list[int]]:
    return sorted([seq for i in range(len(input_data), 0, -1)
                for seq in combinations(input_data, i)
                if sum(seq) == max_size], key=lambda x: len(x))

def part_one(input_data: list[list[int]]) -> int:
    return len(input_data)

def part_two(input_data: list[list[int]]) -> int:
    return sum(len(data) == len(input_data[0]) for data in input_data)

if __name__ == "__main__":
    pod = day.PuzzleOfTheDay(2015, 17)
    input_data = list(map(int, pod.input_data.splitlines()))
    eggnog_exces = 150
    all_combinations = get_all_size_combinations(input_data, eggnog_exces)
    pod.submit("a", part_one(all_combinations))
    pod.submit("b", part_two(all_combinations))