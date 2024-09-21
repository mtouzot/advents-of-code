#!/usr/bin/python
from  .. import day
from typing import Generator
from hashlib import md5

"""
Year 2015 - Day 4 : The Ideal Stocking Stuffer
Solves the December 4th 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_04
"""


def mine_adventcoins(input_data:str) -> Generator[tuple[str,int], None, None]:
        """
        Genereates a range of MD5 hash given an secret key followed by a decimal number
        :return: the MD5 hash with the corresponding decimal number
        :rtype: tuple[str, int]
        """
        for value in range(int(10E6)):
            secret_key = f"{input_data}{value}".encode()
            yield md5(secret_key).hexdigest(), value

def validate(input_data:str,
             zero_padding: int) -> int:
    """
    Validates the MD5 hash if it starts with `zero_padding` zeros then
    returns the corresponding lowest decimal key
    :return: the lowest decimal number validating MD5 hash condition
    :rtype: int
    """
    for hash, value in mine_adventcoins(input_data):
        if hash[:zero_padding] == '0' * zero_padding:
            return value

if __name__ == "__main__":
    pod = day.PuzzleOfTheDay(2015, 4)
    pod.submit("a", validate(pod.input_data, 5))
    pod.submit("b", validate(pod.input_data, 6))
