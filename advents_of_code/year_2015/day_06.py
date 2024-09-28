#!/usr/bin/python
from .. import day
import re

"""
Year 2015 - Day 6 : Probably a Fire Hazard
Solves the December 6th 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_06
"""


def clamp_min(lights_grid: list[int],
              min: int = 0) -> list[int]:
    for nrow in range(len(lights_grid)):
        for ncol in range(len(lights_grid[0])):
            if lights_grid[nrow][ncol] < min:
                lights_grid[nrow][ncol] = min
    return lights_grid

def clamp_max(lights_grid: list[int],
            max: int = 1) -> list[int]:
    for nrow in range(len(lights_grid)):
        for ncol in range(len(lights_grid[0])):
            if lights_grid[nrow][ncol] > max:
                lights_grid[nrow][ncol] = max
    return lights_grid

def clamp(lights_grid: list[int],
          min: int = 0,
          max: int = 1):
    lights_grid = clamp_min(lights_grid, min)
    return clamp_max(lights_grid, max)

def add(lights_grid: list[int],
        start_point: tuple[int, int] = (0, 0),
        end_point:  tuple[int, int] = (0, 0),
        step: int = 0) -> list[int]:
    for nrow in range(start_point[0], end_point[0]+1):
        for ncol in range(start_point[1], end_point[1]+1):
            lights_grid[nrow][ncol] += step
    return lights_grid

def toggle(lights_grid: list[int],
           start_point: tuple[int, int] = (0, 0),
           end_point:  tuple[int, int] = (0, 0)) -> list[int]:
    for nrow in range(start_point[0], end_point[0]+1):
        for ncol in range(start_point[1], end_point[1]+1):
            lights_grid[nrow][ncol] = 1 - lights_grid[nrow][ncol]
    return lights_grid

def part_one(input_data: list[str],
             lights_grid: list[int]) -> int:
    """
    Count the final floor Santa arrives at
    :return: the floor Santa arrives at
    :rtype: int
    """
    for command in input_data:
        start_x, start_y, end_x, end_y = [int(digit) for digit
                                            in re.findall("\d+", command)]
        if "turn on" in command:
            lights_grid = add(lights_grid,
                              (start_x, start_y),
                              (end_x, end_y),
                              1)
            lights_grid = clamp(lights_grid)
        elif "turn off" in command:
            lights_grid = add(lights_grid,
                              (start_x, start_y),
                              (end_x, end_y),
                              -1)
            lights_grid = clamp(lights_grid)
        else:
            lights_grid = toggle(lights_grid,
                                 (start_x, start_y),
                                 (end_x, end_y))
            lights_grid = clamp(lights_grid)
    return sum([sum(lights_grid[nrow]) for nrow in range(len(lights_grid))])

def part_two(input_data: list[str],
             lights_grid: list[int]) -> int:
    """
    :return: the position that causes Santa to first enter the basement
    :rtype: int
    """
    for command in input_data:
        start_x, start_y, end_x, end_y = [int(digit) for digit
                                            in re.findall("\d+", command)]
        if "turn on" in command:
            lights_grid = add(lights_grid,
                              (start_x, start_y),
                              (end_x, end_y),
                              1)
        elif "turn off" in command:
            lights_grid = add(lights_grid,
                              (start_x, start_y),
                              (end_x, end_y),
                              -1)
            lights_grid = clamp_min(lights_grid)
        else:
            lights_grid = add(lights_grid,
                              (start_x, start_y),
                              (end_x, end_y),
                              2)
    return sum([sum(lights_grid[nrow]) for nrow in range(len(lights_grid))])

if __name__ == "__main__":
    pod = day.PuzzleOfTheDay(2015, 6)
    input_data = pod.input_data.splitline()
    square_size = 1000
    init_lights_grid = [[0] * square_size for _ in range(square_size)]
    pod.submit("a", part_one(input_data, init_lights_grid))
    init_lights_grid = [[0] * square_size for _ in range(square_size)]
    pod.submit("b", part_two(input_data, init_lights_grid))