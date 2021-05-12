# de Bruijn assembly option
import argparse
import networkx as nx
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

    # print("bef")
    # print(G.nodes)
    # print("aft")

    # print(G.degree())
    # print("aft2")

    odds = []
    for i in G.degree():
        if i[1] % 2 == 1:
            odds.append(i)

    # print(odds)
    if len(odds) != 2:
        print(-1)
        return
    
    startNode = odds[1][0]
    if G.out_degree(odds[1][0]) < G.in_degree(odds[1][0]):
        startNode = odds[0][0]
    # print(start)


    # print(G.out_edges(start))

    output = startNode
    currentNode = startNode
    while True:
        edges = G.out_edges(currentNode)

        if len(edges) == 0:
            break

        outNodes = [x[1] for x in edges]
        if currentNode in outNodes:
            output += currentNode[-1]
            G.remove_edge(currentNode, currentNode)
            continue
        
        nextnode = list(edges)[0]
        # print(list(edges))
        oldcurr = currentNode
        currentNode = nextnode[1]
        output += currentNode[-1]
        G.remove_edge(oldcurr, currentNode)

    print(output)
    # print(len(output))

dbg()