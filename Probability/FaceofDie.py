import numpy as np
from collections import Counter


def find_interval(x, cum_weights):
    for i in range(0, len(cum_weights)):
        if x < cum_weights[i]:  # Find index to
            return i - 1
    return -1


def weight_choices(face_of_die, weight_of_die):
    # find cumulative weights of the given weights
    cum_weights = [0] + np.cumsum(weight_of_die)
    x = np.random.random()
    print(x)
    # find interval between the cumulative weights
    index = find_interval(x, cum_weights)
    print("Outcome is : ", face_of_die[index])
    return face_of_die[index]


# Die has 6 faces 1,2,3,4,5,6
face_of_die = [1, 2, 3, 4, 5, 6]
# Give sample weights to each die.
weight_of_die = [1 / 12, 1 / 6, 1 / 6, 1 / 6, 3 / 12, 1 / 6]
# Now find the outcome of dice when we throw dice for 100 times.
outcomes = []
for i in range(100):
    outcomes.append(weight_choices(face_of_die, weight_of_die))
    ''' This will maintain counter as dictionary values like key and value.
     Here key is the face of die, value is number of times that face repeats '''
    print(outcomes)
    c = Counter(outcomes)
    print(c)

for key in c:
    c[key] /= 100
print((c.values()))
