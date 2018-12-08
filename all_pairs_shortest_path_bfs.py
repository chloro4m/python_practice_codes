#all pairs shortest path problem
#use BFS to get shortest path form each vertex to every other one

from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')

def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())

#traverse(g.getVertex('sage'))

#main():
g = Graph()

g.addEdge('a','b')
g.addEdge('b','c')
g.addEdge('b','e')
g.addEdge('c','f')
g.addEdge('d','b')
g.addEdge('d','g')
g.addEdge('e','a')
g.addEdge('e','d')
g.addEdge('f','h')
g.addEdge('g','e')
g.addEdge('h','i')
g.addEdge('i','f')

g.addEdge('b','a')
g.addEdge('c','b')
g.addEdge('e','b')
g.addEdge('f','c')
g.addEdge('b','d')
g.addEdge('g','d')
g.addEdge('a','e')
g.addEdge('d','e')
g.addEdge('h','f')
g.addEdge('e','g')
g.addEdge('i','h')
g.addEdge('f','i')
