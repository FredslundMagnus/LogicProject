from game import Game, Players

game = Game(Players.Computer, Players.Computer, Players.Computer)

game.current_beliefs()

for round in range(1, 6):
    print(f"Round {round}!")
    for i in range(3):
        game.update(i, Game.sample())
    game.current_beliefs()
    shared = [None, None, None]
    for i in range(3):
        shared[i] = game.share_card_count(i)
    for i in range(3):
        game.hear_card_count(shared)
    game.current_beliefs()