from __future__ import annotations
from graph import Graph
from enum import Enum
from random import sample, choice
from search import search
from state import State
from copy import deepcopy


class Players(Enum):
    Computer: bool = True
    Human: bool = False


class Game:
    def __init__(self, player1: Players, player2: Players, player3: Players, do_print: bool = True, rounds: int = 3, depth: int = 3) -> None:
        self.graph: Graph = Graph()
        self.states_backup = self.graph.states
        self.players = {0: player1, 1: player2, 2: player3}
        self.rounds: int = rounds
        self.do_print: bool = do_print
        self.depth: int = depth
        self.start()
        if do_print:
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
        print(f"Player {player+1} shares that he is certain about the position of {n} cards.")
        return n

    def __len__(self) -> int:
        return self.rounds

    def __getitem__(self, key: int) -> int:
        if key < self.rounds:
            self.current_beliefs()
            print(f"\nRound {key + 1}!")
            return key + 1
        else:
            self.current_beliefs()
            print("The game is over.\n")
            self.get_scores()
            raise StopIteration

    def format_graph(self) -> dict[State, list[set[State]]]:
        formatted: dict[State, list[set[State]]] = {}
        for state in self.graph.states:
            formatted[state] = []
            for player in range(3):
                formatted[state].append([s for s in self.graph.states if s.cards[player] == state.cards[player]])
        return formatted

    def search(self, depth: int = 3):
        formatted = self.format_graph()
        for player in range(3):
            a = []
            for assumption in [True, False]:
                a.append(search(formatted, possible_states=formatted[self.graph.state][player], dept=depth, player=player, assume_guess=assumption))
            yield a

    def guess(self, should_guess: list[list[bool]]):
        self.should_guesses = []
        for player, should_guesses in enumerate(should_guess):
            if self.players[player] == Players.Human:
                try:
                    guess = [eval("{" + v + "}") for v in input("State your guess 1,1|2,2|3,3 or None: ").split("|")]
                except Exception:
                    yield None
                    continue
                if len(guess) == 1:
                    yield None
                    continue
                try:
                    yield [s for s in self.states_backup if s.cards[0] == guess[0] and s.cards[1] == guess[1] and s.cards[2] == guess[2]][0]
                except Exception:
                    yield guess
            else:
                do_guess = choice(should_guesses)
                self.should_guesses.append(should_guesses)
                guess = choice([s for s in self.graph.states if s.cards[player] == self.graph.state.cards[player]])
                yield guess if do_guess else None

    def get_scores(self):
        correct = []
        for player, guess in enumerate(self.guess(self.search(self.depth))):
            correct.append(guess == self.graph.state if guess != None else None)
            print(f"Player {player} guesses: {guess}" + (f", this is {guess == self.graph.state}" if guess != None else ""))
        print(f"The real state is {self.graph.state}")

        mapping = {None: -1 if any(correct) else 0, True: 1, False: -1}
        self.scores = [mapping[b] for b in correct]
        for i, score in enumerate(self.scores):
            print(f"Player {i+1} got a score of {score}.")
