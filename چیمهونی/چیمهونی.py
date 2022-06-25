# https://quera.org/problemset/28949/

from datetime import time
from collections import Counter


def getInput():
    enter_Exit = []
    n = input()
    for i in range(int(n)):
        i = input()
        enter_Exit.append(i)

    return enter_Exit


def Time2Secend(time):
        result = ((int(time.hour) * 3600) + int(time.minute) + int(time.second))
        return result
    

def BusiesTime(enter_Exit):
    names = set()
    for passing in enter_Exit:
        names.add(passing.split(" ")[0])
    
    # print(enter_Exit) 
    times = {}
    CompareTwoTime = []
    Name_TMP = None
    for name in names:
        for passing in enter_Exit:
            if name in passing:
                CompareTwoTime.append(passing.split(" ")[1:])
                Name_TMP = name

        times.setdefault(Name_TMP, CompareTwoTime)
        
        CompareTwoTime = []
        Name_TMP = None
    
    print(times)
    #___________________
    # {'alish': [['16:15', '+'], ['23:56', '-']], 'pasha': [['21:21', '+'], ['22:34', '-']]}

    
    portion = 10
    interval = 60

    counter = Counter()

    for line in ,.split("\n"):
        time = line.split()[-1]
        hour, minute, second = map(int, time.split(':'))
        since_midnight = hour * 60 + minute
        counter[since_midnight // portion] += 1

    for slot, count in counter.most_common():
        print("%02d:%02d -> %02d:%02d - %d" % ((slot * portion) / 60,
                                            (slot * portion) % 60,
                                            ((slot + 1) * portion) / 60,
                                            ((slot + 1) * portion) % 60,
                                            count))
    
    
BusiesTime(getInput())
