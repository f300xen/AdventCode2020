def check_if_tree(line, x):
    return line[x] == "#"

def loop_through_map(treemap):
    trees = 0
    x = 0
    xSize = len(treemap[0])
    for i in range(len(treemap)):
        if check_if_tree(treemap[i], x):
            trees = trees + 1
        x = (x + 3) % (xSize - 1)
    return trees

treemap = []

with open('input.txt', 'r') as reader:
    for line in reader:
        treemap.append(line)

print(loop_through_map(treemap))
