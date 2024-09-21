#!/usr/bin/python
from .. import day
import re

"""
Year 2015 - Day 5 : Doesn't He Have Intern-Elves For This?
Solves the December 5th 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_05
"""


def at_least_n_voyels(word: str,
                      nb_min_voyels: int) -> bool:
    """
    Validates word containing at least three voyels
    :return: True if word has at least three voyels
    :rtype: bool
    """
    return len(re.findall(r"[aeiou]", word)) >= nb_min_voyels

def twice_in_a_row(word: str) -> bool:
    return len(re.findall(r"(.)\s?\1", word)) > 0

def missing_from(word: str) -> bool:
    return len(re.findall(r"(ab)|(cd)|(pq)|(xy)", word)) == 0

def at_least_two_pairs(word: str) -> bool:
    pairs = re.findall(r"(..).*?(\1)", word)
    return len(pairs) > 0

def at_least_one_rep_with_one_sep(word: str) -> bool:
    return len(re.findall(r"(.)(.)\1", word)) > 0

def part_two(self) -> int:
    """
    :return: the position that causes Santa to first enter the basement
    :rtype: int
    """
    return 

if __name__ == "__main__":
    pod = day.PuzzleOfTheDay(2015, 5)
    input_data = pod.input_data.split("\n")

    answer_a = sum([at_least_n_voyels(word, nb_min_voyels=3)
                    & twice_in_a_row(word)
                    & missing_from(word)
                    for word in input_data])
    pod.submit("a", answer_a)

    answer_b = sum([at_least_two_pairs(word)
                    & at_least_one_rep_with_one_sep(word)
                    for word in input_data])
    pod.submit("b", answer_b)