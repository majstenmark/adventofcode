import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import run, run_samples
from util import multisplit, lazy_ints
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: '))
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def get_day(): return date.today().day
def get_year(): return date.today().year
def db(a):
    if DB: print(a)

def p1(v):
    lines = v.strip().split('\n')
    print('Len input: {} lines {} chars'.format(len(lines), len(v)))

    return 0

def p2(v):
    lines = v.strip().split('\n')
    
    return 0


def manual():
    v = open("real.txt", 'r').read().strip('\n')
    res1 = p1(v)
    res2 = p2(v)
    print('part_1: {}'.format(res1))
    print('part_2: {}'.format(res2))

S = "run samples"
SO = "samples only"
IO = "input only"
FF = "force fetch"
DB = 1
PR = "print input"


if __name__ == '__main__':
    cmds = {S, 
    #'submit1',
    #'submit2' 
    }
    run_samples(p1, p2)
    run(get_year(), get_day(), p1, p2, cmds)
    #manual()
