from Labyrinth import Labyrinth
from Path import Path, Directions

graph = [
    {'E': {'letter': 'I', 'position': Directions.RIGHT}},
    {'I': {'letter': 'N', 'position': Directions.RIGHT}},
    {'I': {'letter': 'J', 'position': Directions.DOWN}},
    {'B': {'letter': 'C', 'position': Directions.DOWN}},
    {'B': {'letter': 'F', 'position': Directions.RIGHT}},
    {'F': {'letter': 'G', 'position': Directions.DOWN}},
    {'J': {'letter': 'O', 'position': Directions.RIGHT}},
    {'O': {'letter': 'R', 'position': Directions.RIGHT}},
    {'O': {'letter': 'P', 'position': Directions.DOWN}},
    {'G': {'letter': 'L', 'position': Directions.RIGHT}},
    {'P': {'letter': 'S', 'position': Directions.RIGHT}},
    {'P': {'letter': 'Q', 'position': Directions.DOWN}},
    {'L': {'letter': 'M', 'position': Directions.DOWN}},
    {'M': {'letter': 'Q', 'position': Directions.RIGHT}},
    {'G': {'letter': 'H', 'position': Directions.DOWN}},
    {'H': {'letter': 'D', 'position': Directions.LEFT}}
]

graph_root = {
    'letter': 'A',
    'connections': [
        {'letter': 'E', 'position': Directions.RIGHT},
        {'letter': 'B', 'position': Directions.DOWN}
    ]
}

lab = Labyrinth(graph_root, graph)
lab.bfs_search('S')
input("press anything to continue.")
lab.dfs_search('S')
input("press anything to continue.")
lab.backtrack_search('S')
