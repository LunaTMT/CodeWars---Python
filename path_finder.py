# https://www.codewars.com/kata/5765870e190b1472ec0022a2/train/python
# Kata Author: evk
# 4 kyu 

import sys
sys.setrecursionlimit(5000)

import numpy as np

def boundary_reached(position, maze):
    i, j = position
    i_max = len(maze) - 1
    j_max = len(maze[0]) - 1

    if (0 <= i <= i_max) and (0 <= j <= j_max):
        return False
    return True 

def check_exit(visited, maze):
    i_max = len(maze) - 1
    j_max = len(maze[0]) - 1

    return True if (i_max, j_max) in visited else False



def check_cardinal(position, maze):
    i, j = position

    card_dict = {
        "N" : (i-1, j),
        "E"  : (i, j+1),
        "S" : (i+1, j),
        "W"  : (i, j-1)
    }

    valid = []
    for key, value in card_dict.items():
        i, j = (value)
        
        if not boundary_reached(value, maze):
            if maze[i][j] == "." or  maze[i][j] == "T":
                valid.append((i, j))
    return valid


def create_graph(maze):
    graph = {}
    
    for (i, j), value in np.ndenumerate(maze):
            if value != "W":   
                graph[(i,j)] = set(check_cardinal((i, j), maze))
                maze[i][j] = "T"
    return graph
           
    
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

def bfs(graph, node): 
    visited = [node] 
    queue = [node]   

    while queue:         
        m = queue.pop(0)
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited


def path_finder(maze):
    maze = np.array([list(row) for row in maze.split('\n')])
    graph = create_graph(maze)
    #visited = dfs(graph, (0,0))
    visited = bfs(graph, (0,0))

    if not check_exit(visited, maze):
        return False
    return True

    
   



if __name__ == "__main__":
    a = "\n".join([
        ".W...",
        ".W...",
        ".W.W.",
        "...W.",
        "...W."])
    path_finder(a)  #, True)
