#!/usr/bin/python
import re
from  .. import day

"""
Year 2015 - Day 14 : Knights of Dinner Table
Solves the December 14th 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_14
"""

def parse_data(input_data: list[str]):
    values = [[int(val) for val in re.findall(r"\d+", data)] for data in input_data]
    return values

def move_reindeers(reindeers, time_max):
    divs = [[time_max // (reindeer[1] + reindeer[2]), min(time_max % (reindeer[1] + reindeer[2]), reindeer[1])]  for reindeer in reindeers]
    return [(divs[index][0]*reindeer[1] + divs[index][1])*reindeer[0] for index, reindeer in enumerate(reindeers)]

def running_reindeers(reindeers, time_max):
    points = [0] * len(reindeers)
    for t in range(1, time_max):
        distances = move_reindeers(reindeers, time_max=t)
        leaders_idx = [idx for idx, dist in enumerate(distances) if dist == max(distances)]
        for idx in leaders_idx:
            points[idx] += 1
    return distances, points

def part_one(input_data: list[str]) -> int:
    return max(running_reindeers(input_data, 2503)[0])

def part_two(input_data: list[str]) -> int:
    return max(running_reindeers(input_data, 2503)[1])

if __name__ == "__main__":
    pod = day.PuzzleOfTheDay(2015, 14)
    input_data = parse_data(pod.input_data.splitlines())
    pod.submit("a", part_one(input_data))
    pod.submit("b", part_two(input_data))