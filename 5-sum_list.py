#!/usr/bin/env python3
"""Write a type-annotated function sum_list which takes a list
input_list of floats as argument and returns their sum as a float.
"""


from typing import List

def sum_list(input: List[float]) -> float:
    """ return their sum of list """
    return float(sum(input_list))
