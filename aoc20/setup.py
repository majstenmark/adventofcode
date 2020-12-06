import sys, time, os
from datetime import date

def get_day(): return date.today().day
def get_year(): return date.today().year

def createfolders(DAY):
    dirname = 'D{}'.format(DAY)
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        for i in range(1, 6):
            open("{}/{}.in".format(dirname, i), "w+")
            
        with open("{}/d{}.py".format(dirname, DAY), "w+") as f:
            
            f.write(open("template.py").read())
        


day = get_day()

if len(sys.argv) > 1:
    day = int(sys.argv[1])
createfolders(day)

