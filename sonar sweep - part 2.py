from itertools import islice

def window(seq, n=2):
    it = iter(seq)
    res = tuple(islice(it, n))
    
    if len(res) == n:
        yield res
    
    for elem in it:
        res = res[1:] + (elem,)
        yield result


data = [int(i) for i in open("input.txt").readlines()]