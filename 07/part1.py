filename='input.txt'

TACHYON_MANIFOLD='S'
SPLITTER='^'
beams=set()
splits=0

with open(filename, 'r') as f:
    topline = f.readline()
    beams.add(topline.find(TACHYON_MANIFOLD))
    for row in f:
        for i in range(len(row)):
            ch = row[i]
            if ch != SPLITTER or i not in beams:
                continue
            beams.remove(i)
            beams.add(i-1)
            beams.add(i+1)
            splits+=1

print(len(beams))
print(beams)
print("splits:",splits)

