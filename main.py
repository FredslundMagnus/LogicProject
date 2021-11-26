from game import Game, Players

game = Game(Players.Computer, Players.Computer, Players.Computer, do_print=True, rounds=2, depth=4)


for round in game:
    for i in range(3):
        game.update(i, Game.sample())
    game.current_beliefs()
    game.share()


print(game.should_guesses)
print(game.scores)
