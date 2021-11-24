
 
states = dict()
for i in range(3):
    for j in range(3):
        for k in range(3):
            states[(i,j,k)] = [set(), set(), set()]
            for l in range(3):
                for p in range(3):
                    states[(i,j,k)][0].add((i,l,p)) 
                    states[(i,j,k)][1].add((l,j,p))
                    states[(i,j,k)][2].add((l,p,k))


def super_search(states, possible_states, player, dept):
    guess = 0
    for state in possible_states:
        guess += guess_search(states, state, dept, player)
    return guess/len(possible_states) >= 0.5


def guess_search(states, state, dept, player):
    possible_states = states[state][player]
    Eg_reward = 2/len(possible_states) - 1
    if Eg_reward >= 0 or dept == 0:
        return True
    Eng_reward = 0
    for assumed_state in possible_states:
        next_guess = []
        prob = []
        for other_player in range(len(states[state])):
            if other_player != player:
                next_guess.append(guess_search(states, assumed_state, dept-1, other_player))
                prob.append(1 / len(states[assumed_state][other_player]))
        Eng_reward += next_guess[0] * next_guess[1] * (1 - prob[0]) * (1 - prob[1]) + next_guess[0] * (1 - next_guess[1]) * (1 - prob[0])
        Eng_reward += next_guess[1] * (1 - next_guess[0]) * (1 - prob[1]) + (1 - next_guess[0]) * (1 - next_guess[1])
    Eng_reward = Eng_reward/len(possible_states) - 1
    print(Eng_reward, possible_states)
    return Eg_reward >= Eng_reward

        
print(states[(0,0,0)][0])
print(super_search(states, possible_states=states[(0,0,0)][0], dept=3, player=0))