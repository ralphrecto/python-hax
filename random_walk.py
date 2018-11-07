import random
from collections import defaultdict

# generator for a random walk of length n
def randwalk(n):
    i = 0
    while i < n:
        yield random.choice([-1, 1])
        i += 1

# computes the probability that the given predicate is satisfied in
# the given number of trials for walks of the given length
def walk_prob(predicate, walk_len, trials=100000):
    walks = (randwalk(walk_len) for i in range(0, trials))
    return sum((1 if predicate(walk) else 0 for walk in walks)) / trials

def never_zero(walk):
    walk_never_zero = True
    accsum = 0
    for x in walk:
        accsum += x
        walk_never_zero &= (accsum != 0)
    return walk_never_zero

# walk_len = 10
# pr(walk ends at origin)
# print(walk_prob(predicate=lambda walk: sum(walk) == 0, walk_len=walk_len))

# pr(walk never goes back to the origin in walk_len steps)
# print(walk_prob(predicate=never_zero, walk_len=walk_len))

# Compute the distribution of the random variable for walks of the given length.
def dist(randvar, walk_len, trials=10000):
    d = defaultdict(int)
    walks = (randwalk(walk_len) for i in range(0, trials))
    for walk in walks:
        v = randvar(walk)
        d[v] = d[v] + 1

    for k in d:
        d[k] = d[k] / trials

    return d

def last_origin_visit(walk):
    last_visit = 0
    curpos = 0
    for i, x in enumerate(walk):
        curpos += x
        if curpos == 0:
            last_visit = i + 1
    return last_visit

print(dist(randvar=last_origin_visit, walk_len=100))
