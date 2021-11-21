from __future__ import annotations
from itertools import permutations

class State:
    @staticmethod
    def isValid(p: list[int]):
        p_set = set(p)
        if 0 in p_set and 1 in p_set and 2 in p_set:
            return False
        if 3 in p_set and 4 in p_set and 5 in p_set:
            return False
        if 6 in p_set and 7 in p_set and 8 in p_set:
            return False
        return True

    def __init__(self, permutation: list[int]) -> None:
        self.state 