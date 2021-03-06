import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *

from collections import defaultdict as dd
#import drawgraph #only works in python3
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: ')) #chars only!
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def db(*a): 
    if DB: print(*a)

def parse(line):
    line = removeall(line,'T','%')
    return lazy_ints(line.split())
    

def p1(v):
    lines = v.strip().split('\n')
    cnt = 0
    data = [parse(line) for line in lines]
    nodes = data[2:]
    pairs = 0
    N= len(nodes)
    for i in range(N):
        for j in range(N):
            if i != j:
                iused = nodes[i][2]
                java = nodes[j][3]
                if iused > 0 and iused <= java:
                    pairs += 1
    return pairs

def p2(v):
    return p1(v)


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    print('part_1: {}\npart2: {}'.format(p1(v), p2(v)))
        
cmds, stats, io, so, DB = get_args(sys.argv)    
if not io: run_samples(p1, p2, cmds)
if not so: run(2016,22, p1, p2, cmds)
if stats: print_stats()
#manual()
