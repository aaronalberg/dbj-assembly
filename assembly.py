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
    
    start = odds[0][0]
    if odds[0][1] < odds[1][1]:
        start = odds[1][0]
    # print(start)


    # print(G.out_edges(start))

    out = start
    curr = start
    while True:
        edges = G.out_edges(curr)

        if len(edges) == 0:
            break
        outs = [x[1] for x in edges]
        if curr in outs:
            out += curr[-1]
            G.remove_edge(curr, curr)
            continue
        
        nextnode = list(edges)[0]
        oldcurr = curr
        curr = nextnode[1]
        out += curr[-1]
        G.remove_edge(oldcurr, curr)

    print(out)

dbg()