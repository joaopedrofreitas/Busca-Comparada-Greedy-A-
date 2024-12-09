import math
from heapq import heappush, heappop
from Graph import node_positions
from Graph import graph

def manhattan_heuristic(node, goal):
    x1, y1 = node_positions[node]
    x2, y2 = node_positions[goal]
    return abs(x1 - x2) + abs(y1 - y2)


def A_Star(graph, start='U', goal='E'):
    open_list = []
    heappush(open_list, (0, start))
    came_from = {}
    
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in graph}
    f_score[start] = manhattan_heuristic(start,goal)

    while open_list:
        _, current = heappop(open_list)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + manhattan_heuristic(neighbor,goal)
                
                heappush(open_list, (f_score[neighbor], neighbor))
    
    return None  


def GBF(graph, start='U', goal='E'):
    open_list = []
    heappush(open_list, (manhattan_heuristic(start,goal), start))
    came_from = {}
    visited = set()

    while open_list:
        _, current = heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        if current in visited:
            continue
        
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                came_from[neighbor] = current
                heappush(open_list, (manhattan_heuristic(neighbor,goal), neighbor))

    return None 
