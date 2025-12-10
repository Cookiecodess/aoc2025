import math
from pprint import pprint

class ThreeCoords():
    x=0
    y=0
    z=0
    def __init__(self, x,y,z):
        self.x = x 
        self.y = y 
        self.z = z 

    def get_coords(self):
        return (x,y,z)

class Solution():

    filename='test.txt'

    coords=[]
    distance_matrix= []
    connected=[]
    circuits=[]

    def __init__(self):
    
        with open(self.filename, 'r') as f:
            for line in f:
                self.coords.append( ThreeCoords(*(int(c) for c in line.strip().split(','))) )

        self.distance_matrix=[[0 for _ in range(len(coords))] for _ in range(len(coords))]
        self.connected=[[False for _ in range(len(coords))] for _ in range(len(coords))]
        
        for i in range(len(coords)):
            for j in range(i+1, len(coords)):
                self.distance_matrix[i][j] = self.distance_matrix[j][i] = euclid_dist(coords[i], coords[j])

    def euclid_dist(coords1: ThreeCoords, coords2: ThreeCoords):
        x1,y1,z1=coords1
        x2,y2,z2=coords2
        return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2) + math.pow(z1-z2, 2))

    def get_closest_coords_pair(self):
        shortest=self.distance_matrix[0][1]
        result=(0,1)
        for i in range(len(self.distance_matrix)):
            for j in range(i+1, len(self.distance_matrix)):
                dist = self.distance_matrix[i][j]
                if dist < shortest and not self.connected[i][j]:
                    shortest= dist
                    result = (i, j)
        return result

    def connect_boxes(self, coords1idx: int, coords2idx: int) -> None:
        self.connected[coords1idx][coords2idx] = self.connected[coords2idx][coords1idx] = True 


    a,b=get_closest_coords_pair(distance_matrix)
    print(coords[a], coords[b])
    connect_boxes(a,b)

    a,b=get_closest_coords_pair(distance_matrix)
    print(coords[a], coords[b])


