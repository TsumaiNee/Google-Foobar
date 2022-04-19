import collections
from typing import TypeVar, Protocol, Optional

Location = TypeVar("Location")

class Graph(Protocol):

    def neighbours(self, id: Location) -> list[Location]: pass

GridLocation = tuple[int,int]

class Grid:

    def __init__(self, width:int, height:int):

        self.width = width
        self.height = height
        self.walls: list[GridLocation] = []

    def in_bounds(self, id: GridLocation) -> bool:

        (x,y) = id
        return (0 <= x < self.width) and (0 <= y < self.height)

    def passable(self, id: GridLocation):

        return id not in self.walls
    
    def neighbours(self, id: GridLocation):

        (x,y) = id
        neighbours = [(x, y+1), (x, y-1), (x+1,y), (x-1,y)]

        if (x+y)%2 == 0: neighbours.reverse()

        results = filter(self.in_bounds, neighbours)
        results = filter(self.passable, results)
        return results

qItem = TypeVar("qItem")

class Queue:

    def __init__(self):
        
        self.elements = collections.deque()
    
    def empty(self) -> bool:

        return not self.elements
    
    def enqueue(self, item: qItem):

        self.elements.append(item)
    
    def dequeue(self) -> qItem:

        return self.elements.popleft()

def bf_search(graph: Grid, start: Location):

    frontier = Queue()
    frontier.enqueue(start)

    origin: dict[Location, Optional[Location]] = {}
    origin[start] = None

    while not frontier.empty():

        current: Location = frontier.dequeue()
        for node in graph.neighbours(current):
            if node not in origin:
                frontier.enqueue(node)
                origin[node] = current
    
    return origin

def path_to(flow_map: dict[Location, Optional[Location]], start: Location, goal: Location):

    current = goal
    path = []
    while current != start:
        path.append(current)
        current = flow_map[current]
    path.append(start)
    return path

def solution(map):
    
    w,h = len(map[0]), len(map)
    walls = []
    for i in range(h):
        for v in range(w):
            if map[i][v] == 1: walls.append((v,i))
    g = Grid(w,h)
    g.walls = walls

    a = bf_search(g, (0,0))
    b = bf_search(g, (w-1,h-1))

    arr = []
    for wall in walls:

        l = []
        for i in g.neighbours(wall):
            if (i in a.keys() or i in b.keys()) and g.in_bounds(i): 
                l.append(len(path_to(a, (0, 0), i)))
                l.append(len(path_to(b, (w-1, h-1), i)))
        if len(l) > 1:
            arr.append(min(i for i in l[::2])+min(i for i in l[1::2])+1)
        print(wall, l, arr)

    for i in map: print(i)
    return min(arr)

solution([[0, 0, 0, 0, 0, 0], 
        [1, 1, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0, 0], 
        [0, 1, 1, 1, 1, 1], 
        [0, 1, 1, 1, 1, 1], 
        [0, 0, 0, 0, 0, 0]])
        
solution([[0, 1, 1, 0], 
        [0, 0, 0, 1], 
        [1, 1, 0, 0], 
        [1, 1, 1, 0]])

solution([[0, 1, 1, 0], 
        [0, 0, 0, 1], 
        [1, 1, 0, 0], 
        [1, 1, 1, 0]])
