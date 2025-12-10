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
        return (self.x, self.y, self.z)


class Solution():

    filename='input.txt'


    coords=[]
    neighbor_map=dict()
    visited=[]
    distance_matrix= []
    connected=[]
    circuits=[]

    def __init__(self):
    
        with open(self.filename, 'r') as f:
            for line in f:
                self.coords.append( ThreeCoords(*(int(c) for c in line.strip().split(','))) )
                #self.circuits.append(set( ThreeCoords(*(int(c) for c in line.strip().split(','))) ))

        self.neighbor_map = { n: set() for n in range(len(self.coords))}
        self.visited = [False for _ in range(len(self.coords))]
        self.distance_matrix=[[0 for _ in range(len(self.coords))] for _ in range(len(self.coords))]
        self.connected=[[False for _ in range(len(self.coords))] for _ in range(len(self.coords))]

        print("Calculating distances...")
        for i in range(len(self.coords)):
            for j in range(i+1, len(self.coords)):
                print(f"\rfor junction box #{i} and junction box #{j}", end="")
                self.distance_matrix[i][j] = self.distance_matrix[j][i] = self.euclid_dist(self.coords[i], self.coords[j])
        print("\nDone calculating distances.")

    def euclid_dist(self, coords1: ThreeCoords, coords2: ThreeCoords):
        x1,y1,z1=coords1.get_coords()
        x2,y2,z2=coords2.get_coords()
        return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2) + math.pow(z1-z2, 2))

    def get_closest_coords_pair(self):
        shortest=self.distance_matrix[0][1]
        result=(0,1)
        for i in range(len(self.distance_matrix)):
            for j in range(i+1, len(self.distance_matrix)):
                dist = self.distance_matrix[i][j]
                if dist < shortest and not self.is_connected(i, j):
                    shortest= dist
                    result = (i, j)
        return result

    def is_connected(self, coords1idx, coords2idx):
        return (
            (coords1idx in self.neighbor_map and coords2idx in self.neighbor_map[coords1idx])
            or 
            (coords2idx in self.neighbor_map and coords1idx in self.neighbor_map[coords2idx])
        )

    def connect_boxes(self, coords1idx: int, coords2idx: int) -> None:
        if coords1idx not in self.neighbor_map:
            self.neighbor_map[coords1idx] = {coords2idx}
        else:
            self.neighbor_map[coords1idx].add(coords2idx)

        if coords2idx not in self.neighbor_map:
            self.neighbor_map[coords2idx] = {coords1idx}
        else:
            self.neighbor_map[coords2idx].add(coords1idx)
        #self.connected[coords1idx][coords2idx] = self.connected[coords2idx][coords1idx] = True 
        #for circ in self.circuits:
        #    if coords1idx in circ:
        #        circ.add(coords2idx)
        #        return
        #self.circuits.append(set(coords1idx, coords2idx))

        

    def count_connected(self, start_node):
        if self.visited[start_node-1]:
            print("Revisited",start_node)
            return 0
        print("Visiting", start_node)
        self.visited[start_node-1] = True 
        accum_count = 1
        print("accum_count:", accum_count)
        neigh = self.neighbor_map[start_node]
        print("Neighbors of", start_node, ":", neigh)
        for n in neigh:
            accum_count += self.count_connected(n)
        return accum_count

    def solve(self):
        if self.filename=='test.txt':
            ITERATIONS=10
        elif self.filename=='input.txt':
            ITERATIONS=1000
        else:
            raise ValueError("invalid filename given")

        print("Connecting junction boxes...")
        for n in range(ITERATIONS):
            print(f"\riteration #{n+1}", end="")
            a,b = self.get_closest_coords_pair()
            self.connect_boxes(a, b)
        print("\nDone connecting junction boxes.")

        print("Calculating circuit sizes...")
        self.visited = [False for _ in range(len(self.coords))]
        circuit_sizes = []
        for i in range(len(self.coords)):
            circuit_sizes.append(self.count_connected(i))
        sorted_circuit_sizes = sorted(circuit_sizes, reverse=True)
        print("\nDone calculating circuit sizes.")
        
        result = 1 
        for i in range(3):
            print(f"#{i+1}: {sorted_circuit_sizes[i]}")
            result *= sorted_circuit_sizes[i]

        print(result)

if __name__=='__main__':
    Solution().solve()
