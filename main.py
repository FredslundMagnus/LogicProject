from __future__ import annotations
from game import Game, Players
from contextlib import redirect_stdout as printer
from sys import stdout as terminal


all_scores: list[list[int]] = []
did_agree: list[list[bool]] = []

n: int = 10
d: int = 5


with printer(None):
    for depth in range(d):
        all_scores.append([])
        did_agree.append([])
        for k in range(n):
            with printer(terminal):
                print(f"{(depth*n+k)/(d*n)*100:.2f}%")
            game = Game(Players.Computer, Players.Computer, Players.Computer, do_print=False, rounds=2, depth=depth)

            for round in game:
                for i in range(3):
                    game.update(i, Game.sample())
                game.current_beliefs()
                game.share()

            all_scores[depth].extend(game.scores)
            did_agree[depth].extend(g[0] == g[1] for g in game.should_guesses)

# print(all_scores)
# print(did_agree)
print("\n\n")
print([sum(a) for a in all_scores])
print([f"{sum(a)/len(a):.2f}" for a in all_scores])
print([sum(a) for a in did_agree])
print([f"{sum(a)/len(a)*100:.2f}%" for a in did_agree])
