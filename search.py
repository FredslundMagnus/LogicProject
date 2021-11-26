



def search(states, possible_states, player, dept, assume_guess):
    Eng_reward = 0
    for state in possible_states:
        Eng_reward += guess_search(states, state, dept, player, assume_guess, return_reward=True)
    return Eng_reward/len(possible_states) <= 2/len(possible_states) - 1


def guess_search(states, state, dept, player, assume_guess, return_reward):
    possible_states = states[state][player]
    Eg_reward = 2/len(possible_states) - 1
    Eng_reward = 0
    if dept > 0:
        for assumed_state in possible_states:
            next_guess = []
            prob = []
            for other_player in range(len(states[state])):
                if other_player != player:
                    next_guess.append(guess_search(states, assumed_state, dept-1, other_player, assume_guess, return_reward=False))
                    prob.append(1 / len(states[assumed_state][other_player]))
            Eng_reward += next_guess[0] * next_guess[1] * (1 - prob[0]) * (1 - prob[1]) + next_guess[0] * (1 - next_guess[1]) * (1 - prob[0])
            Eng_reward += next_guess[1] * (1 - next_guess[0]) * (1 - prob[1]) + (1 - next_guess[0]) * (1 - next_guess[1])
        Eng_reward = Eng_reward/len(possible_states) - 1
    if return_reward:
        return Eg_reward if assume_guess else Eng_reward
    if Eg_reward >= 0 or Eg_reward >= Eng_reward:
        return True
    if dept == 0:
        return assume_guess
    else:
        return False

        
if __name__ == "__main__":
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

    print(states[(0,0,0)][0])
    print(search(states, possible_states=states[(0,0,0)][0], dept=3, player=0, assume_guess=True))