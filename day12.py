
from collections import defaultdict
import sys

directions = [(1,0),(-1,0),(0,1),(0,-1)]

def get_grid():
    with open("./inputs/day12_input.txt","r") as file:
        return [list(line.strip()) for line in file]
    
def is_already_in_region(pos_and_val: tuple[int,int,str], regions: set[set[tuple[int]]]):
    for entry in regions:
        if pos_and_val in entry:
            return True
    return False

def find_region(pos_and_val: tuple[int,int,str], graph: dict, regions: set[frozenset[tuple[int,int,str]]]) -> frozenset[tuple[int,int,str]]:
    region = set()
    visited = set()
    elem = pos_and_val[2]
    stack = []
    stack.append(pos_and_val)  

    while len(stack) != 0:
        node = stack.pop()

        if node in visited:
            continue
        
        visited.add(node)
        
        if node[2] == elem and not is_already_in_region(node,regions):
            region.add(node)
        
        children = graph.get(node)

        if children == None:
            continue

        for child in children:
            if child not in visited:
                stack.append(child)

    return frozenset(region)

def get_area(region: frozenset[tuple[int,int,str]]) -> int:
    return len(region)

def get_perimeter(region: frozenset[tuple[int,int,str]]) -> int:
    # If there is no adjacent point --> there is a perimeter!
    perimeters = 0
    for i,j,val in region:
        for r,c in directions:
            r,c = tuple(map(sum, zip((i,j),(r,c))))
            if not (r,c,val) in region:
                perimeters += 1
    return perimeters


def get_sides(region: frozenset[tuple[int,int,str]]) -> int:
    return sum(map(lambda x : get_corner_nodes(region, x), region))
    
    
def get_corner_nodes(wall_nodes, node) -> int:
    corners = 0
    y,x ,val = node
    
    top, bot = (y -1, x, val) ,(y + 1, x, val)
    left, right = (y, x-1, val), (y, x +1, val)
    diag_top_left ,diag_top_right = (y-1, x-1,val), (y-1, x +1, val)
    diag_bot_left, diag_bot_right = (y+1, x-1,val), (y+1, x+1, val)

    # A corner can either be a "inner-corner" or a "outer-corner"
    
    # Add top left corner to node: *A
    if left not in wall_nodes and top not in wall_nodes or (
        top in wall_nodes and left in wall_nodes and diag_top_left not in wall_nodes
    ):
        corners += 1
    
    # Add top right corner to node: A*
    if right not in wall_nodes and top not in wall_nodes or (
        top in wall_nodes and right in wall_nodes and diag_top_right not in wall_nodes
    ):
        corners += 1

    # Add bottom left corner to node _A
    if left not in wall_nodes and bot not in wall_nodes or (
        left in wall_nodes and bot in wall_nodes and diag_bot_left not in wall_nodes
    ):
        corners += 1

    # Add bottom right corner to node A_

    if right not in wall_nodes and bot not in wall_nodes or (
        right in wall_nodes and bot in wall_nodes and diag_bot_right not in wall_nodes
    ):
        corners += 1

    return corners

def main():
    grid = get_grid()
    regions = set(frozenset()) # set of all regions, each region contains all the points in it
    
    # Convert to graph
    # All of the adjacent with the same char have an edge between them
    graph = defaultdict(list)
    # Create a edge to each of its surrounding chars and also store how many unlike elements it has beside
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            elem = grid[i][j]
            graph[(i,j,elem)] = list()
            for r,c in directions:
                r,c = tuple(map(sum, zip((i,j),(r,c))))
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == elem:
                    graph[(i,j,elem)].append((r,c,elem))
    
    for node in graph.keys():
        if not is_already_in_region(node,regions):
            regions.add(find_region(node,graph,regions))

    
    price = sum(map(lambda region: get_area(region) * get_perimeter(region), regions))
    print(f"Part 1: {price}")
    # Ans: 1381056

    price = sum(map(lambda region: get_area(region) * get_sides(region), regions))
    print(f"Part 2: {price}")
    # Ans: 834828
 
if __name__ == "__main__":
    main()
