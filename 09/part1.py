filename="input.txt"

coords=[]
with open(filename, "r") as f:
    for line in f:
        coords.append([int(x) for x in line.strip().split(",")])


largest_x = coords[0][0]
smallest_x = coords[0][0]
for i in range(len(coords)):
    x = coords[i][0]
    y = coords[i][1]
    if x > largest_x:
        largest_x = x
    elif x < smallest_x:
        smallest_x = x
# for largest_x, find largest y
largest_y_diff = 0
for i in range(len(coords)):
    if coords[i][0] != largest_x:
        continue
    print(coords[i][0], "lagrets")
    for j in range(len(coords)):
        if coords[j][0] != smallest_x:
            continue
        print(coords[j][0], "smoles")
        y_diff = abs(coords[i][1] - coords[j][1])
        print(coords[i][1], coords[j][1])
        if y_diff > largest_y_diff:
            largest_y_diff = y_diff
        
width = largest_x - smallest_x + 1
height = largest_y_diff + 1
area1 = width * height
print(width, height)
print(area1)





largest_y = coords[0][1]
smallest_y = coords[0][1]
for i in range(len(coords)):
    x = coords[i][0]
    y = coords[i][1]
    if y > largest_y:
        largest_y = y
    elif y < smallest_y:
        smallest_y = y
# for largest_y, find largest x diff
largest_x_diff = 0
for i in range(len(coords)):
    if coords[i][1] != largest_y:
        continue
    print(coords[i][1], "lagrets")
    for j in range(len(coords)):
        if coords[j][1] != smallest_y:
            continue
        print(coords[j][1], "smoles")
        x_diff = abs(coords[i][0] - coords[j][0])
        print(coords[i][0], coords[j][0])
        if x_diff > largest_x_diff:
            largest_x_diff = x_diff
        
width = largest_x_diff + 1
height = largest_y - smallest_y + 1
area2 = width * height

print("area1:",area1)
print("area2:",area2)













