# returns total as checksum
# input - string
from functools import reduce

def checksum(st):
    return reduce(lambda x,y:x+y, map(ord, st))

# returns total mod 256 as checksum
# input - string
def checksum256(st):
    return reduce(lambda x,y:x+y, map(ord, st)) % 256

# totals a list of numbers
# input - list or tuple of numbers
def totalList(lst):
    return reduce(lambda x,y:x+y, lst)

# returns the average of a list of numbers
# input - list or tuple of numbers
def averageList(lst):
    return reduce(lambda x,y:x+y, lst) / len(lst)

def check(st, checkSum):
    return (reduce(lambda x, y: x + y, map(ord, st)) - checkSum)