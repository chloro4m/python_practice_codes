# All Pairs Shortest Path Implementation

import sys

# key are vertices; each edge has weight and that's encoded as well
graph = {0: {1: 2, 4:4},
         1: {2:3},
         2: {3:5, 4:1 },
         3: {0: 8},
         4: {3:3}}

def allPairsShortestPath(g):
    """Return distance structure as computed"""
    #dist+pred will be dicts (key:vtx, val:dict->KEY:toVtx, VAL:dist/pred) 
    dist = {}
    pred = {}
    #for all vertices, create dict values with vertex as key
    for u in g: 
        dist[u] = {} 
        pred[u] = {}
        #for all vertices, set init. dist+pred to all vertices, including self
        for v in g: 
            dist[u][v] = sys.maxsize
            pred[u][v] = None

        #finish off init with obvious dist and pred to self as 0 and None
        dist[u][u] = 0
        pred[u][u] = None

        #for all vertices in graph for current vertex u, set obvious..
        #..neighboring direct dist and pred
        for v in g[u]:
            dist[u][v] = g[u][v]
            pred[u][v] = u

    #this is the heavy lifting to figure out...
    for mid in g:
        for u in g:
            for v in g:
                newlen = dist[u][mid] + dist[mid][v]
                if newlen < dist[u][v]:
                    dist[u][v] = newlen
                    pred[u][v] = pred[mid][v]

    return (dist,pred)
        
def constructShortestPath(s, t, pred):
    """Reconstruct shortest path from s to t using information in pred"""
    path = [t]

    while t != s:
        t = pred[s][t]
        
        if t is None:
            return None
        path.insert(0, t)
    
    return path

##That is, graph is a dictionary whose keys are the vertices and the value is itself
##a dictionary of vertex : weight pairs. Thus in the above representation, there
##are two edges emanating from vertex 0: (0,1) and (0,4). Edge (0,1) has a weight
##of 2 while edge (0,4) has a weight of 4.
##
##With such a graph, invoke allPairsShortestPath and be prepared to receive a 
##dist and pred matrix containing the solution
##
##   >>> dist, pred = allPairsShortestPath(graph)
## 
##The dist structure is a two-dimensional dictionary whose value dist[i][j] represents
##the minimum cost of any path between vertices i and j. pred[i][j] represents the 
##previous vertex to use when traversing the shortest path from vertex i to j. To 
##recover the solutions, invoke following:
##
##   >>> constructShortestPath(s, t, pred)
##
##where s and t are vertices in the graph and pred is the structure returned by 
##allPairseShortestPath


#random example of dynamic programming:
past_fib = {}

def fibonacci(n):
    """Return nth fibonacci number memorizing past solutions"""

    if n in past_fib:
        return past_fib[n]
    
    if n == 0 or n == 1:
        past_fib[n] = 1
        return 1

    total = fibonacci(n-1) + fibonacci(n-2)
    past_fib[n] = total
    return total
