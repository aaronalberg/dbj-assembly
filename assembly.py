# de Bruijn assembly option
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('reads')
args = parser.parse_args()

with open(args.reads) as reads_fh:
  reads = reads_fh.read().splitlines()

nodes = set()
edges = []

kmers = []

lefts = []
rights = []

for i in reads:
    

    left = i[:-1]
    right = i[1:]

    kmers.append(left)
    kmers.append(right)
    edges.append((left,right))

#     lefts.append(left)
#     rights.append(right)

#     nodes.add(left)
#     nodes.add(right)

# nodes = list(nodes)

# for i in range(len(kmers)):
#     for j in range(i + 1, len(kmers)):
#         if i is j:
#             continue

#         k1 = kmers[i]
#         k2 = kmers[j]
#         print(k1[1:])
#         if k1[1:] == k2[:-1]:
#             edges.append((k1, k2))
#         if k1[:-1] == k2[1:]:
#             edges.append((k2, k1))


# print(nodes)
# print(lefts)
# print(rights)


    # edge = (left, right)
    # nodes.add(left)
    # nodes.add(right)
    # edges.append((left, right))

# print(reads[0][:-1])
# print(reads[0][1:])

print(edges)

n = len(edges)
for i in range(n):
    for j in range(i + 1, n):
        if i == j:
            continue
        right = edges[i][1]
        left = edges[j][0]
        if right == left:
            edges.append((right, left))
            
print(edges)
print(len(edges))
