filename='test.txt'

TACHYON_MANIFOLD='S'
SPLITTER='^'
beams=set()

with open(filename, 'r') as f:
    topline = f.readline()
    beams.add(topline.find(TACHYON_MANIFOLD))
    for row in f:
        for i in range(len(row)):
            ch = row[i]
            if ch != SPLITTER:
                continue



