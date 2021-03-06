from __future__ import annotations
from state import State
from itertools import permutations, product
from random import choice

class Graph:
    def __init__(self) -> None:
        self.states: list[State] = [State(p) for p in permutations(range(9),6) if State.isValid(p)]
        # self.edges: dict[tuple[State, State], set[int]] = {(a, b): Graph.start_edges(a,b) for a, b in product(self.states, self.states)}
        self.state: State = choice(self.states)
        # print(len(self.states), len(self.states)//6)
        # print(len(self.edges), len(self.edges)//36)
        # print(len([1 for e in self.edges.values() if e]))
        # print('m',len([s for s in self.states if 0 in s.beliefs]))

    @staticmethod
    def start_edges(a: State, b: State) -> set[int]:
        temp = ((i,(a.cards[i], b.cards[i])) for i in range(3))
        return {i for i, (cards_a, cards_b) in temp if cards_a == cards_b}

    def start(self):
        for state in self.states:
            for player, cards in self.state.cards.items():
                if state.cards[player] != cards:
                    state.beliefs = {p for p in state.beliefs if p != player}

    def update(self, player: int, cards: set[int], answer: bool):
        states: list[State] = []
        for state in self.states:
            temp = len([card for card in state.cards[player] if card in cards]) > 0
            if temp == answer:
                states.append(state)
        self.states = states

    def player_beliefs(self, player: int) -> list[State]:
        return [s for s in self.states if player in s.beliefs]

    @staticmethod
    def info_about_clique(clique: list[State]) -> tuple[int, set[int], set[int], set[int], set[int]]:
        try:
            table = set.intersection(*[s.table for s in clique])
            player1 = set.intersection(*[s.cards[0] for s in clique])
            player2 = set.intersection(*[s.cards[1] for s in clique])
            player3 = set.intersection(*[s.cards[2] for s in clique])
            n = sum([len(s) for s in [table, player1, player2, player3]])
        except TypeError:
            return 0, set(), set(), set(), set()
        return n, table, player1, player2, player3

    def hear_cards_count(self, shared: list[int]):
        self.states = [state for state in self.states if self.fits(state, shared)]

    def fits(self, state: State, was_shared: list[int]) -> bool:
        states: list[list[State]] = []
        for i in range(3):
            states.append([s for s in self.states if s.cards[i] == state.cards[i]])
        would_have_been_shared = [Graph.info_about_clique(clique)[0] for clique in states]
        return all([a==b for a, b in zip(would_have_been_shared, was_shared)])

                

        
        
