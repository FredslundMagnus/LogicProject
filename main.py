from __future__ import annotations
from game import Game, Players
from contextlib import redirect_stdout as printer
from sys import stdout as terminal
import numpy as np
from pickle import dump
all_scores: list[list[int]] = []
did_agree: list[list[bool]] = []

n: int = 1
d: int = 5


# with printer(None):
for depth in range(5):
    all_scores.append([])
    did_agree.append([])
    if depth != 4:
        continue
    for k in range(n):
        # with printer(terminal):
        #     print(f"{(depth*n+k)/(d*n)*100:.2f}%")
        game = Game(Players.Human, Players.Computer, Players.Computer, do_print=False, rounds=3, depth=depth)
        print(game.graph.state.cards[0])
        for round in game:
            for i in range(3):
                game.update(i, Game.sample())
            game.current_beliefs()
            # game.share()

        all_scores[depth].extend(game.scores)
        did_agree[depth].extend(g[0] == g[1] for g in game.should_guesses)


all_scores = all_scores[-1:]
did_agree = did_agree[-1:]
print("\n\n")
print(all_scores)
print(did_agree)
print("\n\n")


print([sum(a) for a in all_scores])
print([f"{sum(a)/len(a):.2f}" for a in all_scores])
print([(1.96 * np.std(a)/np.sqrt(len(a)))/len(a) for a in all_scores])
print([sum(a) for a in did_agree])
print([f"{sum(a)/len(a)*100:.2f}%" for a in did_agree])
print([(1.96 * np.std(a)/np.sqrt(len(a)))/len(a) for a in did_agree])


# with open("all_scores_3.pickle", 'wb') as f:
#     dump(all_scores, f)

# with open("did_agree_3.pickle", 'wb') as f:
#     dump(did_agree, f)
