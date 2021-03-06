import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    return int(line)

def p1(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    cnt = 0
    data = [parse(line) for line in lines]
    data.append(0)

    data.append(max(data)+ 3)
    data.sort()
    #one
    diffs = [0] * 4
    for i in range(len(data)-1):
        d = data[i+1] - data[i]
        diffs[d] += 1
    db(diffs)
    return diffs[1] * diffs[3]



def p2(v):
    lines = v.strip().split('\n')
    chunks = v.strip().split('\n\n')
    data = [parse(line) for line in lines]
    data.append(0)
    data.append(max(data)+ 3)
    data.sort()
    dp = defaultdict(int)
    dp[0] = 1
    alt = [1, 2, 3]
    for i in range(len(data)):
        volt = data[i]
        cnt = dp[volt]
        for a in alt:
            v2 = volt + a
            dp[v2] += cnt
    return dp[data[-1]]




def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2020,10, p1, p2, cmds)
if stats: print_stats()
#manual()
