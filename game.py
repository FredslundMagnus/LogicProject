from __future__ import annotations
from graph import Graph
from enum import Enum
from random import sample

from state import State

class Players(Enum):
    Computer: bool = True
    Human: bool = False


class Game:
    def __init__(self, player1: Players, player2: Players, player3: Players, do_print: bool = True, rounds: int = 3) -> None:
        self.graph: Graph = Graph()
        self.players = {0: player1, 1: player2, 2: player3}
        self.rounds: int = rounds
        self.do_print: bool = do_print
        self.start()
        if do_print: print(self)


    def start(self) -> None:
        self.graph.start()

    @staticmethod
    def sample() -> set[int]:
        return set(sample(range(9), 3))

    def update(self, player: int, cards: set[int]) -> None:
        # if self.players[player] == Players.Computer:
        answer = len([card for card in self.graph.state.cards[player] if card in cards]) > 0

        self.graph.update(player, cards, answer)


        print(f"Player {player+1} was asked if he had one of the cards {cards}, he said {answer}")

    def __str__(self) -> str:
        return f"Player 1: {self.graph.state.cards[0]}, Player 2: {self.graph.state.cards[1]}, Player 3: {self.graph.state.cards[2]}, Table: {self.graph.state.table}"

    def current_beliefs(self) -> None:
        if not self.do_print:
            return
        beliefs: dict[int, list[State]] = {}
        for i in range(3):
            beliefs[i] = [s for s in self.graph.states if i in s.beliefs]
            print(f"Player {i+1} has {len(beliefs[i])} states.", end=' ')
        print(f'Total States: {len(self.graph.states)}')
        for i in range(3):
            n, table, player1, player2, player3 = Graph.info_about_clique(beliefs[i])
            print(f"Player {i+1} is certain of {n} cards:    Player 1: {player1}, Player 2: {player2}, Player 3: {player3}, Table: {table}")

    def share(self) -> None:
        shared = [None, None, None]
        for i in range(3):
            shared[i] = self.share_card_count(i) if self.players[i] == Players.Computer else int(input("How many cards do you know? "))
        self.graph.hear_cards_count(shared)

    def share_card_count(self, player: int) -> int:
        # if self.players[player] == Players.Computer:
        n, *_ = Graph.info_about_clique(self.graph.player_beliefs(player))
        print(f"Player {player+1} shares that he is sertain about the position of {n} cards.")
        return n

    def __len__(self) -> int:
        return self.rounds

    def __getitem__(self, key: int) -> int:
        if key < self.rounds:
            print(f"\nRound {key + 1}!")
            return key + 1
        else:
            raise StopIteration

    
            
            