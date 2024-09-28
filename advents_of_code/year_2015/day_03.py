#!/usr/bin/python
from  .. import day
from typing import Generator

"""
Year 2015 - Day 3 : Perfectly Spherical Houses in a Vacuum
Solves the December 3rd 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_03
"""

def next_visited_house(input_data,
                        current_point: tuple[int, int] = (0, 0),
                        starting_move: int = 1,
                        step: int = 1) -> Generator[tuple[int, int], None, None]:
    direction = {
        '^': (0, 1),
        'v': (0, -1),
        '<': (-1, 0),
        '>': (1, 0),
    }
    for way in input_data[starting_move::step]:
        current_point = tuple(map(lambda x, y: x + y,
                                  current_point,
                                  direction[way]))
        yield current_point

def part_one(input_data: str):
    start_at = (0, 0)
    reached_points = {point for point in next_visited_house(input_data,
                                                            start_at)}
    reached_points.add(start_at)
    return len(reached_points) + 1 

def part_two(input_data: str):
    start_at = (0, 0)
    santa_locations = {point for point in next_visited_house(input_data,
                                                             start_at,
                                                             starting_move=0,
                                                             step=2)}
    santa_locations.add(start_at)
    robot_locations = {point for point in next_visited_house(input_data,
                                                             start_at,
                                                             starting_move=1,
                                                             step=2)}
    robot_locations.add(start_at)
    return len(santa_locations | robot_locations)

def main():
    pod = day.PuzzleOfTheDay(2015, 3)
    pod.submit("a", part_one(pod.input_data))
    pod.submit("b", part_two(pod.input_data))


if __name__ == "__main__":
    main()
