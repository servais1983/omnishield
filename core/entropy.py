from math import log2

def calculate_entropy(s):
    prob = [float(s.count(c)) / len(s) for c in set(s)]
    return -sum([p * log2(p) for p in prob])
