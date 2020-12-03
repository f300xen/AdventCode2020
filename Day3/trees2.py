def check_if_tree(line, x):
    return line[x] == "#"

def loop_through_map(treemap, right, down):
    trees = 0
    x = 0
    xSize = len(treemap[0])
    for i in range(0, len(treemap), down):
        if check_if_tree(treemap[i], x):
            trees = trees + 1
        x = (x + right) % (xSize - 1)
    return trees

treemap = []

with open('input.txt', 'r') as reader:
    for line in reader:
        treemap.append(line)

print(loop_through_map(treemap, 1, 1))
print(loop_through_map(treemap, 3, 1))
print(loop_through_map(treemap, 5, 1))
print(loop_through_map(treemap, 7, 1))
print(loop_through_map(treemap, 1, 2))
