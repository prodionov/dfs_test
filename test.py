import random
import sys

#number of nodes
#n = int(sys.stdin.readline())
#num_nodes = random.randint(1, n)

#enter number of components for testing purposes
#num_comp = int(sys.stdin.readline())

#generate graph with that number of components

def generate_graph(num_comp):
    graph = {}
    last_vertex = 0
    for i in range(num_comp):
        #print 'component: ', i
        #"""create strongly connected commponent"""
        num_nodes = random.randint(1, 100)
        #print 'num_nodes', num_nodes
        for y in range(num_nodes):
            connections = set([ver for ver in range(last_vertex + 1, last_vertex + num_nodes + 1) if ver != (y + last_vertex + 1)])
            #print 'connections', connections
            graph[y + last_vertex + 1] = [False, connections]
            #print 'graph', graph        
        last_vertex += num_nodes 
        #print 'last_vertex', last_vertex
    return graph

#graph = generate_graph(num_comp)    
#max possible number of nodes is n*(n-1)/2
#unfortunatly, that generates a dense graph with 1 connected component
#num_edges = random.randint(0, num_nodes * (num_nodes - 1) / 2)

#for the purpose of the test we will generate a sparse graph
#|E| = |V| 
#num_edges = num_nodes

#print 'num_nodes', num_nodes, ' num_edges', num_edges

#initiate graph 
#graph = {i : [False, set()] for i in range(1, num_nodes + 1)}
#print graph

#generate edges
#it's a simple graph, there should be no loops 
#list_of_edges = []

#while len(list_of_edges) < num_edges:
#    start = random.randint(1, num_nodes)
#    end = random.randint(1, num_nodes)
#    if start != end and set([start, end]) not in list_of_edges:
#        list_of_edges.append(set([start, end]))

#adding edges into the graph
#for edge in list_of_edges:
#    beg = list(edge)[0]
#    end = list(edge)[1]
#    graph[beg][1].add(end)
#    graph[end][1].add(beg)

#print graph    

#we need a slow, but a robust algorithm for testing purposes
def dfs_slow(graph):
    graph_test = dict(graph)
    visited = []
    components = 0
    for vertex in graph_test.keys():
        if vertex not in visited:
            visited.extend(list(graph[vertex][1]))
            components += 1
    return components


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


correctness = True
while correctness:
    num_components = random.randint(0, 1000)
    graph = generate_graph(num_components)
    algorithm_output = dfs_alg(graph)
    #print graph 
    if algorithm_output == num_components:
        print 'correct'
    else:
        print 'something is not right'
        print 'num_components', num_components
        print 'algorithm output', algorithm_output
        
