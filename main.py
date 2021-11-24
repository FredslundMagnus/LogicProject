from game import Game, Players

game = Game(Players.Computer, Players.Computer, Players.Computer, do_print=True, rounds=4)

game.current_beliefs()
for round in game:    
    for i in range(3):
        game.update(i, Game.sample())
    game.current_beliefs()
    game.share()
    print(game.graph.states)
    game.current_beliefs()