import collections

filename='input.txt'

TACHYON_MANIFOLD='S'
SPLITTER='^'
beams=set()
splits=0
timelines={}

def add(dic, key, val):
    if key not in dic:
         dic[key] = 0
    dic[key] += val

def split_timelines(dic, col):
    timelines = dic[col]
    dic[col] = 0
    add(dic, col-1, timelines)
    add(dic, col+1, timelines)

with open(filename, 'r') as f:
    topline = f.readline()
    beams.add(topline.find(TACHYON_MANIFOLD))
    timelines[topline.find(TACHYON_MANIFOLD)] = 1
    for row in f:
        for i in range(len(row)):
            ch = row[i]
            if ch != SPLITTER or i not in timelines:
                continue
            split_timelines(timelines, i)
            print(timelines)

print(sum(timelines.values()))

