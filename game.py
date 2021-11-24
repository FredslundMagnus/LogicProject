from __future__ import annotations
from graph import Graph
from enum import Enum
from random import sample

from state import State

class Players(Enum):
    Computer: bool = True
    Human: bool = False


class Game:
    def __init__(self, player1: Players, player2: Players, player3: Players) -> None:
        self.graph: Graph = Graph()
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.players = {0: player1, 1: player2, 2: player3}
        self.start()
        print(self)

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
        beliefs: dict[int, list[State]] = {}
        for i in range(3):
            beliefs[i] = [s for s in self.graph.states if i in s.beliefs]
            print(f"Player {i+1} has {len(beliefs[i])} states.", end=' ')
        print('')
        for i in range(3):
            n, table, player1, player2, player3 = Graph.info_about_clique(beliefs[i])
            print(f"Player {i+1} is certain of {n} cards:    Player 1: {player1}, Player 2: {player2}, Player 3: {player3}, Table: {table}")
        print('')

    def share(self) -> None:
        shared = [None, None, None]
        for i in range(3):
            shared[i] = self.share_card_count(i)
        self.graph.hear_cards_count(shared)

    def share_card_count(self, player: int) -> int:
        # if self.players[player] == Players.Computer:
        n, *_ = Graph.info_about_clique(self.graph.player_beliefs(player))
        print(f"Player {player+1} shares that he is sertain about the position of {n} cards.")
        return n

    
            
            