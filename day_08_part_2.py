forest = [list(map(int, tree)) for tree in open('day_08_input.txt').read().splitlines()]

scenic_score = 0
for tree_line in range(len(forest)):
    for tree in range(len(forest[tree_line])):
        current_tree = forest[tree_line][tree]
        L = R = U = D = 0
        for x in range(tree - 1, -1, -1):
            L += 1
            if forest[tree_line][x] >= current_tree:
                break
        for x in range(tree + 1, len(forest[tree_line])):
            R += 1
            if forest[tree_line][x] >= current_tree:
                break
        for x in range(tree_line - 1, -1, -1):
            U += 1
            if forest[x][tree] >= current_tree:
                break
        for x in range(tree_line + 1, len(forest)):
            D += 1
            if forest[x][tree] >= current_tree:
                break

        scenic_score = max(scenic_score, L * R * U * D)

print(scenic_score)