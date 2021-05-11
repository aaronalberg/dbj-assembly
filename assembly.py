# de Bruijn assembly option
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('reads')
args = parser.parse_args()

with open(args.reads) as reads_fh:
  reads = reads_fh.read().splitlines()

nodes = []
edges = []

out = reads[0]
isFirst = True
for i in reads:
    if isFirst:
        isFirst = False
        continue
    out += i[-1]


    # left = i[:-1]
    # right = i[1:]
    # tup = (left, right)
    # edges.append(tup)

  

# print(reads[0][:-1])
# print(reads[0][1:])
# print(edges)
print(out)