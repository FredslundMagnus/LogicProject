from game import Game, Players

game = Game(Players.Computer, Players.Computer, Players.Computer, do_print=False, rounds=4)

game.current_beliefs()
for round in game:    
    for i in range(3):
        game.update(i, Game.sample())
    game.current_beliefs()
    game.share()
    game.current_beliefs()