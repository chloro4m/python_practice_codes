#modify DFS code to give Strongly Connected Components

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

    def dfsvisitSCC(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                print(nextVertex.getId())
                nextVertex.setPred(startVertex)
                self.dfsvisitSCC(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

    #to finish code, need to print each node per tree per dfs forest!
    def scc_dfs(self, vtxList): #my helper code, called on gT
##        print("Now inside the 'gT.scc_dfs(res)' call.")
##        print("This is the vtxList passed in, should be sorted (finTime, VertObj) of dfs(g).")
##        print(vtxList)
##        print(vtxList[0][1].getId())
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for item in vtxList: #vtxList item: (finTime, VertObj)
            v_id = item[1].getId()
            scc_vtx = self.getVertex(v_id)
            if scc_vtx.getColor() == 'white': #bug, need to refer to gT verts
                print("These are SCC's: ")
                print(scc_vtx.getId())
                self.dfsvisitSCC(scc_vtx) 

    def scc(self): #my code
        #find gT
        gT = DFSGraph()
        for v in self:
           for w in v.getConnections():
               gT.addEdge(w.getId(), v.getId())
        #call dfs on g
        self.dfs()
        #call dfs on gT, but main loop of DFS explore vtx in
        #decreasing order of finish time:
        finish_times = []
        for aVertex in self:
            finish_times.append((aVertex.getFinish(), aVertex))
        res = sorted(finish_times, key = lambda x: x[0], reverse = True)
        gT.scc_dfs(res)
        return gT
    
#main():
g = DFSGraph()
g.addEdge('a','b')
g.addEdge('b','c')
g.addEdge('b','e')
g.addEdge('c','c')
g.addEdge('c','f')
g.addEdge('d','b')
g.addEdge('d','g')
g.addEdge('e','a')
g.addEdge('e','d')
g.addEdge('f','h')
g.addEdge('g','e')
g.addEdge('h','i')
g.addEdge('i','f')

gT_dfs = g.scc()
##print("Check that this is indeed gT:")
##for v in gT_dfs:
##    print("vertex: %s neighbors: %s"\
##          %(v.getId(), [x.getId() for x in v.getConnections()]))
print("\nResults of scc algo: ")
for v in gT_dfs:
    if v.getPred() != -1:
        print("Vert: %s Start: %s Fin: %s Pred: %s"%\
              (v.getId(), v.getDiscovery(), v.getFinish(),\
               v.getPred().getId()))
    elif v.getPred() == -1:
        print("Vert: %s Start: %s Fin: %s Pred: None"%\
              (v.getId(), v.getDiscovery(), v.getFinish()))
    else:
        print("Uh oh bug!!!")
