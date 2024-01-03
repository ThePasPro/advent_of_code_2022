forest = [list(map(int, line)) for line in open('day_08_input.txt').read().splitlines()]

visible_trees = 0

for index_tree_line, tree_line in enumerate(forest):
    for index_tree, tree in enumerate(tree_line):
        current_tree = forest[index_tree_line][index_tree]
        if all(forest[index_tree_line][x] < current_tree for x in range(index_tree)) or all(forest[index_tree_line][x] < current_tree for x in range(index_tree + 1, len(forest[index_tree_line]))) or all(forest[x][index_tree] < current_tree for x in range(index_tree_line)) or all(forest[x][index_tree] < current_tree for x in range(index_tree_line + 1, len(forest))):
            visible_trees += 1

print(visible_trees)