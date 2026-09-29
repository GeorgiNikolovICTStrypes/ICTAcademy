"""
This is an implementation of the Djistra algorithm
"""
import heapq

def get_path(parent_array, target):
    """
    Given a parent and a source and target it returns the path by going back using the
    Parent array
    Inputs:
     parent_array: |V| sized array of integers
     source: integer - starting vertex
     target: integer - destination vertex
    Outputs:
     Path: A |V| sized array of integers - path from source to target
    """
    path = []
    while target is not None:
        path.append(target)
        target = parent_array[target]
    path.reverse()
    return path

def djikstra(adj, source, target= None):
    """
    Returns the distance from source to target in a weighted graph with no negative
    weights. If target = None returns the distance from source to all other vertices.
    Inputs:
     adj - |V| sized list of lists of tuples (vertex, weight): An adjacency matrix representation of a graph.
     source - Starting vertex
     target - target vertex
    Outputs:
     result - int/float - Distance from source to target or
     distances - |V| sized list of distances. 
     if dist[i] for any i that means that i is not reachable from source 
    """
    
    n = len(adj)
    parent = [None for _ in range(n)]
    distances = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    distances[source] = 0
    queue = [(0, source)]
    while queue:
        curr_distance, curr_vertex = heapq.heappop(queue)
        if visited[curr_vertex]:
            continue
        visited[curr_vertex] = True
        for neigh, neigh_cost in adj[curr_vertex]:
            if neigh_cost + curr_distance < distances[neigh]:
                distances[neigh] = neigh_cost + curr_distance
                parent[neigh] = curr_vertex
                heapq.heappush(queue, (distances[neigh], neigh))
    
    if target is not None:
        print(get_path(parent,target))
        return distances[target]
    return distances

if __name__ ==  '__main__':
    adj = [[(1,4), (2,1)], [(3,1)], [(1,2), (3,5)], []]
    assert djikstra(adj,0) == [0,3,1,4]
    assert djikstra(adj,0,3) == 4
    assert djikstra(adj,1) == [float("inf"), 0 , float("inf"), 1]

