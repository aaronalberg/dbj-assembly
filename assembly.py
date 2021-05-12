# de Bruijn assembly option
import argparse
import networkx as nx
from networkx.algorithms.components.connected import is_connected
from networkx.classes.function import to_undirected
# import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument('reads')
args = parser.parse_args()

with open(args.reads) as reads_fh:
  reads = reads_fh.read().splitlines()

def dbg():

    G = nx.MultiDiGraph()

    edges = []
    for i in reads:
        left = i[:-1]
        right = i[1:]
        edges.append((left,right))
        G.add_edge(left, right)


    odds = []
    for i in G.degree():
        if i[1] % 2 == 1:
            odds.append(i)

    # Eulerian trail requires exactly 2 nodes of odd degree
    if len(odds) != 2:
        print(-1)
        return
    
    # start with node that has more out edges than in edges
    startNode = odds[1][0]
    if G.out_degree(odds[1][0]) < G.in_degree(odds[1][0]):
        startNode = odds[0][0]


    output = startNode
    currentNode = startNode
    while True:
        G.remove_nodes_from(list(nx.isolates(G)))
        edges = G.out_edges(currentNode)

        if len(edges) == 0:
            break

        outNodes = [x[1] for x in edges]
        if currentNode in outNodes:
            output += currentNode[-1]
            G.remove_edge(currentNode, currentNode)
            continue

        for i in list(edges):
            nextnode = i
            oldcurr = currentNode
            currentNode = nextnode[1]
            G.remove_edge(oldcurr, currentNode)
            G.remove_nodes_from(list(nx.isolates(G)))

            # at the final node
            if (nx.is_empty(G)):
                output += currentNode[-1]
                break

            # if removed edge is a bridge, add it back and try the next edge
            if not (nx.is_connected(G.copy().to_undirected())):
                G.add_edge(oldcurr, currentNode)
                currentNode = oldcurr
            else:
                output += currentNode[-1]
                break

    print(output)

dbg()