from __future__ import annotations
from state import State
from itertools import permutations

class Graph:
    def __init__(self) -> None:
        self.states: list[State] = []
        for p in (list(p) for p in permutations(range(9),6) if State.isValid(list(p))):
            self.states.append(State(p))