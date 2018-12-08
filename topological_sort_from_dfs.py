#modify DFS code into a topological sort

from pythonds.graphs import Graph
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

    #my code
    def topological_sort(self):
        self.dfs()
        finish_times = []
        for aVertex in self:
            finish_times.append((aVertex.getFinish(), aVertex.getId()))
        res = sorted(finish_times, key = lambda x: x[0], reverse = True)
        print("Here's the result of topological sort: ")
        print(res)

#main
dfsG = DFSGraph()

dfsG.addEdge('a', 'd')       
dfsG.addEdge('b', 'd')       
dfsG.addEdge('c', 'd')      
dfsG.addEdge('d', 'e')      
dfsG.addEdge('e', 'g')      
dfsG.addEdge('g', 'i')      
dfsG.addEdge('i', 'k')      
dfsG.addEdge('d', 'f')     
dfsG.addEdge('f', 'h')      
dfsG.addEdge('h', 'j')     
dfsG.addEdge('j', 'k')

dfsG.topological_sort()
                                
        
