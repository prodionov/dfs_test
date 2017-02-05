#python2
import sys

var = sys.stdin.readline()
var = map(int, var.strip('').split(' '))

n = var[0]
m = var[1]

graph = {i : [False, set()] for i in range (1, n+1)}



#creating the graph
for i in range(m):
    edge = sys.stdin.readline()
    edge = map(int, edge.strip('').split(' '))
    beg = edge[0]
    end = edge[1]
    graph[beg][1].add(end)
    graph[end][1].add(beg)

def dfs_alg(graph):
    cc = 0
    for ver in graph.keys():
        #print 'dfs, Vertex:', ver
        #print 'true or false', graph[ver][0]
        if not graph[ver][0]:
            #print 'going to explore', ver
            explore(graph, ver)
            #print 'adding +1 to cc'
            cc += 1
    return cc

def explore(graph, vertex):
    #print 'explore function'
    #print vertex
    graph[vertex][0] = True
    for ver in graph[vertex][1]:
        if not graph[ver][0]:
            explore(graph, ver)

print dfs_alg(graph)
