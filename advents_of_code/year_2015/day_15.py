#!/usr/bin/python
import re
from math import prod
from itertools import permutations
from  .. import day

"""
Year 2015 - Day 15: Science for Hungry People
Solves the December 15th 2015 Advent of Code puzzles

How to run:
    python -m advents_of_code.year_2015.day_15
"""

def parse_data(input_data: list[str]) -> list[list[int]]:
    properties = []
    for data in input_data:
        *_, props = data.split(": ")
        props = re.findall(r"-*\d+", props) # extract all numbers from string
        properties.append(list(map(int, props))) # convert found numbers to int
    return list(map(list, zip(*properties))) # gather by properties instead of ingredients

def compute_score(input_data: list[list[int]],
                  teaspoon_weights: list[int],
                  activation: list[int]):
    properties_scores = [sum([a*b for a,b in zip(prop, teaspoon_weights)]) for prop in input_data]
    return prod([score * active for score, active in zip(properties_scores, activation) if active * score > 0])

def generate_teaspoon_weights(N,S):
    result = set()
    
    # Fonction récursive pour trouver les combinaisons
    def backtrack(current_combination, remaining_sum, start):
        if len(current_combination) == N:
            if remaining_sum == 0:  # On vérifie si la somme de la combinaison vaut S
                for comb in permutations(current_combination[:]):
                    result.add(comb)  # On ajoute une copie de la combinaison
            return
        
        for i in range(start, remaining_sum + 1):
            current_combination.append(i)
            backtrack(current_combination, remaining_sum - i, i)
            current_combination.pop()  # On retire le dernier élément pour explorer une autre combinaison

    backtrack([], S, 0)
    return result

def part_one(input_data: list[str]):
    nb_of_ingredients = len(input_data[0])
    activation_weights = [1] * (len(input_data) - 1) + [0]
    all_scores = []
    for teaspoon_weights in generate_teaspoon_weights(nb_of_ingredients, 100):
        all_scores.append(compute_score(input_data, teaspoon_weights, activation_weights))
    return max(all_scores)

def part_two(input_data: list[str]):
    nb_of_ingredients = len(input_data[0])
    activation_weights = [1] * (len(input_data) - 1) + [0]
    all_scores = []
    for teaspoon_weights in generate_teaspoon_weights(nb_of_ingredients, 100):
        if compute_score(input_data, teaspoon_weights, [0, 0, 0, 0, 1]) == 500:
            all_scores.append(compute_score(input_data, teaspoon_weights, activation_weights))
    return max(all_scores)

if __name__ == "__main__":
    pod = day.PuzzleOfTheDay(2015, 15)
    input_data = parse_data(pod.input_data.splitlines())
    pod.submit("a", part_one(input_data))
    pod.submit("b", part_two(input_data))