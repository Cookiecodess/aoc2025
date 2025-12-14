filename="input.txt"

coords=[]
with open(filename, "r") as f:
    for line in f:
        coords.append([int(x) for x in line.strip().split(",")])

largest_area=0
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        x1 = coords[i][0]
        y1 = coords[i][1]
        x2 = coords[j][0]
        y2 = coords[j][1]
        curr_area = abs(x1-x2+1) * abs(y1-y2+1)
        if curr_area > largest_area:
            largest_area = curr_area
            
print(largest_area)