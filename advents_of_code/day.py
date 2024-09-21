#!/usr/bin/python
from aocd import submit
from aocd.models import Puzzle

class PuzzleOfTheDay(Puzzle):
    def __init__(self, year, day, user=None):
        super().__init__(year, day, user)

    def submit(self, part, solution):
        submit(day=self.day,
               year=self.year,
               part=part,
               answer=solution)
