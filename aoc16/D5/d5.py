import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from fetch import *
from util import *
import hashlib
#lo, hi, lt, pw = lazy_ints(multisplit(line, '-: '))
#or lo, hi, lt, pw = lazy_ints(multisplit(line, ['-',': ','))
import re
#use regex re.split(' |,|: ', line)

def get_day(): return 5# date.today().day
def get_year(): return 2016# date.today().year
def db(*a):
    if DB: print(*a)

def p1(v):
    id = v.strip()
    i = 1
    pw = []
    while True:
        ha = id + str(i)
        r = hashlib.md5(ha.encode()).hexdigest()
        if r.startswith('00000'):
            pw.append(r[5])
            db(r[5],  len(pw))
            if len(pw) == 8:
                return ''.join(pw)
        i += 1

    return ''.join(pw)

def p2(v):
    id = v.strip()
    i = 1
    pw = [''] * 8
    used = set()
    while True:
        ha = id + str(i)
        r = hashlib.md5(ha.encode()).hexdigest()
        if r.startswith('00000'):
            pos = int(r[5]) if r[5].isdigit() else -1

            val = r[6]
            if 0<= pos < 8 and pw[pos] == '':
                pw[pos] = val
                used.add(pos)
                db(pos, val)
            if len(used) == 8:
                return ''.join(pw)
        i += 1

    return ''.join(pw)


    return 0



def manual():
    v = open("real.txt", 'r').read().strip('\n')
    res1 = p1(v)
    res2 = p2(v)
    print('part_1: {}'.format(res1))
    print('part_2: {}'.format(res2))

FF = "force fetch"
DB = 0
PR = "print input"
so = 0
io = 0
stats = 0
cmds = []

def get_args():
    global stats, so, io, DB    
    for arg in sys.argv[1:]:
        if arg == 'f':
           cmds.append(FF)
        if arg == 's1' or  arg == '1':
           cmds.append("submit1")
        if arg == 's2' or arg == '2':
           cmds.append("submit2")
        if arg == 'p' or arg == 'pi':
           cmds.append(PR)
        if arg == 'so':
            so = 1
        if arg == 'io':
            io = 1
        if arg == 'db':
            DB = 1
        if arg == 'st' or arg == 'stat' or arg == 'stats':
            stats = 1
        if arg == 'p1' or arg == 'part1':
            cmds.append('p1')
        if arg == 'p2' or arg == 'part2':
            cmds.append('p2')
        

if __name__ == '__main__':
    get_args()
    if not io: run_samples(p1, p2, cmds)
    if not so: run(get_year(),  get_day(), p1, p2, cmds)
    if stats: print_stats()
    #manual()
