import re
import itertools
import numpy as np

#Python zip version
def count_doubles_zip(val):
    total = 0
    for c1, c2 in zip(val, val[1:]):
        if c1 == c2:
            total += 1
    return total

#Python classic count
def count_doubles_classic(val):
    total = 0
    for i in range(len(val)-1):
        if val[i] == val[i+1]:
            total += 1
    return total

#Python iter count
def count_doubles_iter(val):
    total = 0
    chars = iter(val)
    c1 = next(chars)
    for c2 in chars:
        if c1 == c2:
            total += 1
        c1 == c2    
    return total

#Python itertools count
def count_doubles_itertools(val):
    c1s, c2s = itertools.tee(val)
    next(c2s, None)
    total = 0
    for c1, c2 in zip(c1s, c2s):
        if c1 == c2:
            total += 1
    return total    

#Python regexp version
double_re = re.compile(r'(?=(.)\1)')

def count_doubles_regexp(val):
    return len(double_re.findall(val))

#Python numpy version
def count_doubles_numpy(val):
    ng = np.frombuffer(bytearray(val, encoding='utf-8'), dtype=np.byte)
    return np.sum(ng[:-1]==ng[1:])

#Python list comprehension version
def count_doubles_comprehension(val):
    return sum(1 for c1, c2 in zip(val, val[1:]) if c1 == c2)
