from game import Game, Players

game = Game(Players.Computer, Players.Computer, Players.Computer, do_print=False, rounds=2, depth=0)


for round in game:
    for i in range(3):
        game.update(i, Game.sample())
    game.current_beliefs()
    game.share()

print(game.should_guesses)
print([g[0] == g[1] for g in game.should_guesses])
print(sum([int(g[0] == g[1]) for g in game.should_guesses]))
print(game.scores)
