#!/usr/bin/python
from .. import day
from math import sqrt
from itertools import islice

"""
Year 2015 - Day 20: Infinite Elves and Infinite Houses
Solves the December 20th 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_20
"""


def divisorGenerator(nth_house: int):
    large_divisors = []
    for i in range(1, int(sqrt(nth_house) + 1)):
        if nth_house % i == 0:
            yield i
            if i*i != nth_house:
                large_divisors.insert(0, int(nth_house/i))
    for divisor in large_divisors:
        yield divisor


def delivered_gifts(nth_house: int,
                    factor: int):
    return factor * sum(divisorGenerator(nth_house))


def part_one(input_data: int):
    index_house = 10
    factor = 10
    while factor * sum(divisorGenerator(index_house)) < input_data:
        index_house += 1
    return index_house


def part_two(input_data: int):
    index_house = 1
    factor = 11
    while factor * sum([div for div in divisorGenerator(index_house) if index_house / div <= 50 ]) < input_data:
        index_house += 1
    return index_house



if __name__ == "__main__":
    pod = day.PuzzleOfTheDay(2015, 20)
    input_data = int(pod.input_data)
    pod.submit("a", part_one(input_data))
    pod.submit("b", part_two(input_data))
