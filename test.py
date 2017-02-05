import random
import sys

""" 
testing code for DFS algorithm

rather than compare DFS algorithm with some slower version that counts number of connected components,
generate_graph function creates a graph with a set number of connected components in it 
final while loop checks whether DFS output the same number of components
"""

def generate_graph(num_comp):
    graph = {}
    last_vertex = 0
    for i in range(num_comp):
        num_nodes = random.randint(1, 100)
        for y in range(num_nodes):
            connections = set([ver for ver in range(last_vertex + 1, last_vertex + num_nodes + 1) if ver != (y + last_vertex + 1)])
            graph[y + last_vertex + 1] = [False, connections]        
        last_vertex += num_nodes 
    return graph


def dfs_alg(graph):
    cc = 0
    for ver in graph.keys():
        if not graph[ver][0]:
            explore(graph, ver)
            cc += 1
    return cc

def explore(graph, vertex):
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
        
