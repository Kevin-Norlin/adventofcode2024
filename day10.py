
from collections import defaultdict


def get_grid() -> list[list[int]]:
    with open("./inputs/day10_input.txt","r") as file:
        return [list(map(int,list(line.strip()))) for line in file]
    
def build_graph(grid: list[list[int]]) -> defaultdict[list]:
    graph = defaultdict(list)
    directions = [(0,1),(0,-1),(1,0),(-1,0)] # right, left, down, up
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            for dir in directions:
                y,x = tuple(map(sum, zip((i,j),dir)))
                if 0 <= y < m and 0 <= x < n and grid[y][x] - grid[i][j] == 1: # One step up
                    graph[(i,j,grid[i][j])].append((y,x, grid[y][x])) # An edge: (i,j) --> (y,x)
    return graph

def dfs(startingNode, nodes: defaultdict) -> int:
    acc = 0
    visited = set()
    stack = []
    stack.append(startingNode)
    while len(stack) != 0:
        node = stack.pop()
        visited.add(node)

        # If there is a 9, there is a path!
        if node[2] == 9:
            acc += 1

        children = nodes.get(node)

        if children == None:
            continue

        for child in children:
            if child not in visited:
                stack.append(child)
    return acc

def bfs(startingNode, nodes: defaultdict) -> int:
    acc = 0
    visited = set()
    stack = []
    stack.append(startingNode)
    while len(stack) != 0:
        node = stack.pop(0)
        visited.add(node)

        # If there is a 9, there is a path!
        if node[2] == 9:
            acc += 1

        children = nodes.get(node)

        if children == None:
            continue

        for child in children:
            if child not in visited:
                stack.append(child)
    return acc
    
def main():
    grid = get_grid()

    # Part 1
    # Model as directed graph, if where 1 -> 2 -> 3 and so on
    graph = build_graph(grid) # Each node: (y,x,val) : edges 

    acc = 0
    # Idea: Do dfs for each 0: 
    for node in graph.keys():
        if node[2] == 0:
            acc += dfs(node,graph)

    print(acc)
    # Ans: 472

    # Part 2
    # In part 2, we can visit the same 9 more than once, as long as the path is slightly different
    # At any point in the traversal we have a choice: 
    # So when there are multiple nodes to choose from, traverse all! --> Bfs
    acc = 0
    for node in graph.keys():
        if node[2] == 0:
            acc += bfs(node,graph)
    print(acc)
    # Ans: 969 

if __name__ == "__main__":
    main()