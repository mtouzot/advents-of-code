#!/usr/bin/python
from  .. import day

"""
Year 2015 - Day 18: Like a GIF For Your Yard
Solves the December 18th 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_18
"""

def neighbors(input_data:list[str],
                          pos: tuple[int] = None):
    if pos is None:
        min_row = min_col = 0
        max_row = len(input_data)
        max_col = len(input_data[0])
    else:
        row, col = pos
        min_row = row - 1 if row > 0 else 0
        max_row = row + 2 if row < len(input_data) else row
        min_col = col - 1 if col > 0 else 0
        max_col = col + 2 if col < len(input_data) else col
    return [data[min_col:max_col] for data in input_data[min_row:max_row]]

def count_on_neighbors(input_data: list[str]):
    return sum([data.count('#') for data in input_data])

def update_neighbors(input_data: list[str],
                         corners=False):
    res = []
    for row in range(0, len(input_data)):
        lights = ''
        for col in range(0, len(input_data[row])):

            if input_data[row][col] == '#':
                if count_on_neighbors(neighbors(input_data, (row, col))) in [3, 4]\
                    or (corners and (row, col) in [(0, 0), (0, len(input_data[row])-1), (len(input_data)-1, len(input_data[row])-1), (len(input_data)-1, 0)]):
                    lights += '#'
                else:
                    lights += '.'
            if input_data[row][col] == '.':
                if count_on_neighbors(neighbors(input_data, (row, col))) == 3:
                    lights += '#'
                else:
                    lights += '.'
        res.append(lights)
    return res

def part_one(input_data: list[str]):
    for _ in range(100):
        input_data = update_neighbors(input_data)
    return count_on_neighbors(input_data)

def part_two(input_data: list[str]):
    for _ in range(100):
        input_data = update_neighbors(input_data, True)
    return count_on_neighbors(input_data) - 4

if __name__ == "__main__":
    pod = day.PuzzleOfTheDay(2015, 18)
    input_data = pod.input_data.splitlines()
    pod.submit("a", part_one(input_data))
    input_data = pod.input_data.splitlines()
    pod.submit("b", part_two(input_data))
