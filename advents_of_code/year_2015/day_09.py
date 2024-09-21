#!/usr/bin/python
from itertools import permutations, islice, tee
from  .. import day

"""
Year 2015 - Day 9 : All in a Single Night
Solves the December 9th 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_09
"""


def compute_all_dists(input_data: list[str]) -> list[int]:
    paths = dict()
    for data in input_data:
        city_A, _, city_B, _, distance = data.split()
        paths.setdefault(city_A, {})[city_B] = paths.setdefault(city_B, {})[city_A] = int(distance)
    return [sum(paths[start][end]
            for start, end in zip(tee(p)[0], islice(tee(p)[1], 1, None)))
            for p in permutations(paths)]

if __name__ == "__main__":
    pod = day.PuzzleOfTheDay(2015, 9)
    input_data = pod.input_data.splitlines()
    distances = compute_all_dists(input_data)
    pod.submit("a", min(distances))
    pod.submit("b", max(distances))
