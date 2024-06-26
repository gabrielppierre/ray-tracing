from point import *

CUBE = {
    "vertices" : [Point(0,0,0),Point(0,-1,0),Point(0,-1,1),Point(0,0,1),Point(1,0,0),Point(1,0,1),Point(1,-1,0),Point(1,-1,1)],
    "triplas" : [(0,1,2),(0,2,3),(0,5,4),(0,3,5),(6,4,7),(5,7,4),(1,6,7),(2,1,7),(3,2,5),(2,7,5),(0,4,1),(1,4,6)]
}

ROOF = {
    "vertices" : [Point(0,0,0),Point(0,-1,0),Point(0,-0.5,1),Point(1,0,0),Point(1,-1,0),Point(1,-0.5,1)],
    "triplas" : [(0,1,2),(5,4,3),(0,2,3),(2,5,3),(1,4,5),(1,5,2),(0,4,1),(4,0,3)]
}