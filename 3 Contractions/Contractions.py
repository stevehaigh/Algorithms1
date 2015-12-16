import copy
import math
import random

# helper method to print a graph
#
def PrintData(graph):
    for item in graph.items():
        print(str(item))

# given 2 node indices and a graph this will merge the 2 nodes and update the graph.
#
def ContractElement(liveNode, deadNode, graph):
    if len(graph) < 2:
        return "ERROR, graph too small!"
    
    # Add all deadNodes edges to liveNode
    graph[liveNode] = graph[liveNode] + graph[deadNode]

    # Remove loops, there must be at least one now, if not throw an error!
    while graph[liveNode].count(liveNode) > 0:
        graph[liveNode].remove(liveNode)

    # remove references to deadNode
    while graph[liveNode].count(deadNode) > 0:
        graph[liveNode].remove(deadNode)

    # For all vertexes on the deadNode go and make them point to the liveNode
    for v in set(graph[deadNode]):
        if v != liveNode:
            while graph[v].count(deadNode) > 0:
                graph[v].remove(deadNode)
                graph[v].append(liveNode)

    # remove the deadNode from the graph
    del(graph[deadNode])
    
    # return the graph
    return graph

# Perform the Karger algorithm on a graph, taking the nodes at random
#
def GetSmallestCutWithRandomSampling(graphIn):

    # copy the graph because we'll wreck it here!
    graph = copy.deepcopy(graphIn)

    # contract the graph until we can do no more
    while len(graph) > 2:
        v, e = GetRandomVertexAndEdge(graph)     
        graph = ContractElement(v, e, graph)        

    # check last 2 vertices have same edge count!
    edges1 = graph[list(graph.keys())[0]]
    edges2 = graph[list(graph.keys())[1]]
    if len(edges1) != len(edges2):
        return 0
    else:
        return len(edges1)

# Select a node at random from the graph, and then a node linked to that node.        
#
def GetRandomVertexAndEdge(graph):
    random.seed()
    randomNodeNumber = random.choice(graph.keys())   
    randomOtherNodeNumber = random.choice(graph[randomNodeNumber])
    return randomNodeNumber, randomOtherNodeNumber


# MAIN
#
if __name__ == "__main__":
    
    f = open("C:\\Users\\shaigh\\Documents\\Dropbox\\Stanford\\Algo\\Algorithms Projects\\3 Contractions\\kargerAdj.txt", "r")
    graph = {}
    for line in f:
        vertexData = line.split()
        node = []
        for item in vertexData:
            node.append(int(item))

        # Add date to a dict, the first element is the node number (== key), the rest are the edges from that node ( == data)
        graph[node[0]] = node[1:]

    f.close()

    # sanity check, take a look at the graph before running
    ## PrintData(graph)
    
    minCut = GetSmallestCutWithRandomSampling(graph)

    # repeat this n^2 * log(n) times and keep best result
    n = len(graph)
    numberOfIterations = int((n^2) * math.log(n))

    print("Running " + str(numberOfIterations) + " iterations")

    for i in range(numberOfIterations):
        m = GetSmallestCutWithRandomSampling(graph)
        ## print("Iteration " + str(i) + " min cut so far = " + str(minCut) + " latest attempt = " + str(m))
        if m < minCut:
            minCut = m

    print("RESULT: MinCut = " + str(minCut))






