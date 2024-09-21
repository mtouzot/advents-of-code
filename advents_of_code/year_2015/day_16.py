#!/usr/bin/python
import re
from  .. import day

"""
Year 2015 - Day 16: Aunt Sue
Solves the December 16th 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_16
"""

def parse_data(input_data: list[str]):
    raw_str = r"Sue (\d+): (.*): (\d+), (.*): (\d+), (.*): (\d+)"
    return [{b: int(c), d: int(e), f: int(g)}
            for data in input_data
            for a, b, c, d, e, f, g in re.findall(raw_str, data)]

def part_one(input_data: list[dict]) -> int:
    global mfcam
    for idx, sue in enumerate(input_data, 1):
        if sue.items() <= mfcam.items():
            return idx

def part_two(input_data: list[dict]) -> int:
    global mfcam
    for idx, sue in enumerate(input_data, 1):
        if all(sue.get(k, mfcam[k]) >= mfcam[k] for k in ["cats","trees"])\
            and all(sue.get(k, mfcam[k]) <= mfcam[k] for k in ["pomeranians", "goldfish"])\
            and all(sue.get(k, mfcam[k]) == mfcam[k] for k in mfcam.keys() if k not in ["cats","trees","pomeranians", "goldfish"]):
            print(sue)
            return idx

if __name__ == "__main__":
    pod = day.PuzzleOfTheDay(2015, 16)
    input_data = parse_data(pod.input_data.splitlines())
    mfcam = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    pod.submit("a", part_one(input_data))
    pod.submit("b", part_two(input_data))