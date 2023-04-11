import math
import itertools

# defining gridworld():
g_space = [
    [0, 0, 0, 1],
    [0, 0, 0, -1],
    [0, 0, 0, 0]]
noise = .2
gamma = .9
action_list = {"U" : (-1, 0), "D" : (1, 0), "R" : (0, 1), "L" : (0, -1)}


# checking if the state is terminal state
def terminal_state(state):
    (i, j) = state
    if i == 0 and j == 3:
        return True
    elif i == 1 and j == 3:
        return True
    return False


# value_space = [[0 for i in range(4)] for j in range(3)]   #the main value space
value_space = [
    [0, 0, 0, 1],
    [0, 0, 0, -1],
    [0, 0, 0, 0]]

# val = sum of (possibility * [reward for state + gamma*reward for next state])
main_p = 1 - noise   # setting the probability
noise_p = noise / 2  # setting the probability
row, col = 3, 4

# not necessary in updated version
# def next_state(state, action):   #To get the next state for a particular action
#     (i, j) = state
#     next_i = i + action_list[action][0]
#     next_j = j + action_list[action][1]
#     if next_i < 0 or next_i >= row or next_j < 0 or next_j >= col :
#         next_i, next_j = i, j
#     return next_i, next_j


def value(state):
    (i, j) = state
    #print(i, j, value_space[i][j])
    return value_space[i][j]

# not necessary in updated version
# def get_value(action, state):
#     (i, j) = state
#     if action == "U":
#         val = main_p * gamma * value(next_state(state, "U")) + noise_p * gamma * value(next_state(state, "L")) + noise_p * gamma * value(next_state(state, "R"))

#     elif action == "R":
#         val = main_p * gamma * value(next_state(state, "R")) + noise_p * gamma * value(next_state(state, "U")) + noise_p * gamma * value(next_state(state, "D"))

#     elif action == "L":
#         val = main_p * gamma * value(next_state(state, "L")) + noise_p * gamma * value(next_state(state, "U")) + noise_p * gamma * value(next_state(state, "D"))

#     elif action == "D":
#         val = main_p * gamma * value(next_state(state, "D")) + noise_p * gamma * value(next_state(state, "L")) + noise_p * gamma * value(next_state(state, "R"))
    
#     return val


def possible_future_states(state):
    i, j = state
    possible_states = {(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i, j)}
    if i==0:
        possible_states.remove((i-1, j))
    if i==3-1:
        possible_states.remove((i+1, j))
    if j==0:
        possible_states.remove((i, j-1))
    if j==4-1:
        possible_states.remove((i, j+1))

    tmp_states = possible_states.copy()
    for x, y in tmp_states:
        if (x, y) == (1, 1):
            possible_states.remove((x, y))

    return possible_states


def transition_probability(state, action):

    i, j = state
    if action == 'U':
        p =  {(i-1, j): main_p, (i, j+1): noise_p, (i, j-1): noise_p, (i, j): 0}
    elif action == 'D':
        p =  {(i+1, j): main_p, (i, j+1): noise_p, (i, j-1): noise_p, (i, j): 0}
    elif action == 'L':
        p =  {(i, j-1): main_p, (i-1, j): noise_p, (i+1, j): noise_p, (i, j): 0}
    elif action == 'R':
        p =  {(i, j+1): main_p, (i-1, j): noise_p, (i+1, j): noise_p, (i, j): 0}

    pfs = possible_future_states(state)
    for state_key in p:
        if state_key not in pfs:
            tmp = p[state_key]
            p[state_key] = 0
            p[state] +=  tmp
    return p


def get_value(action, state):
    """
    Returns the value of a state
    """
    val = 0
    p = transition_probability(state, action)
    for state_key in p:
        if(p[state_key]):
            val += p[state_key] * gamma * value_space[state_key[0]][state_key[1]]
    return val

best_actions = [[None]*4 for i in range(3)]

for iters in range(50):
    #new_value_space = [[0]*4 for i in range(3)]
    for i in range(3):
        for j in range(4):
            state = (i, j)
            if terminal_state(state) or state == (1, 1):
                pass

            else:
                max_v = -math.inf
                for action in action_list:
                    state_v = get_value(action, (i, j))
                    if state_v > max_v:
                        max_v = state_v
                        best_a = action

                value_space[i][j] = max_v
                best_actions[i][j] = best_a


# print(value_space)
# print(best_actions)

final_data = {}    #combining value and action

for (i, j) in itertools.product(range(3), range(4)):
    final_data[i,j] = [value_space[i][j], best_actions[i][j]]

print(f"The final value and actions for particular cell: {final_data}")


#-----------------------visualizing the data-------------------------------


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


data = np.array(value_space)
text = np.array(best_actions)
  
# combining text with values
formatted_text = (np.asarray(["{0}\n{1:.2f}".format(
    text, data) for text, data in zip(text.flatten(), data.flatten())])).reshape(3, 4)
 
# drawing heatmap
fig, ax = plt.subplots()
colormap = sns.color_palette("Purples") 
ax = sns.heatmap(data, annot=formatted_text, fmt="", cmap=colormap)

plt.show()