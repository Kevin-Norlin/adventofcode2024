
# Conditions for antinode: 
# Appears when two antennas of same freq are in perfect line 
# BUT only when 1 of the antennas is 2x as far away as the other FROM the antinode.
# Calc distance with pythagoras? 

import math

def get_grid() -> list[list[str]]:
    with open("./inputs/day8_input.txt","r") as file:
        # We want it in list list str

        return [list(line.strip()) for line in file]

def get_distance(p1: tuple[int], p2: tuple[int]) -> tuple[int]:
    r_diff, c_diff = p2[0] - p1[0] , p2[1] - p1[1]
    return (r_diff, c_diff)

def find_antinodes(grid, r, c, antinodes):
    antenna = grid[r][c]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if (r,c) == (i,j):
                continue
            if grid[i][j] == antenna:
                r_diff, c_diff = get_distance((r,c),(i,j))
                nr, nc = r + r_diff + r_diff, c + c_diff + c_diff
                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and (nr,nc) not in antinodes:
                    antinodes.add((nr,nc))
            
def find_antinodes_with_harmonics(grid, r, c, antinodes):
    antenna = grid[r][c]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if (r,c) == (i,j):
                continue
            if grid[i][j] == antenna:
                r_diff, c_diff = get_distance((r,c),(i,j))
                n = 0
                while True: 
                    nr, nc = r + r_diff * n, c + c_diff * n
                    if nr < 0 or nr > len(grid) -1 or nc < 0 or nc > len(grid[0]) -1:
                        break

                    if (nr,nc) not in antinodes:
                        antinodes.add((nr,nc))
                        
                    n += 1
 
def main():
    grid = get_grid()
    antinodes = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != ".":
                find_antinodes(grid, r, c, antinodes)
    
    print(f"Part 1: {len(antinodes)}")
    # Ans: 265

    grid = get_grid()
    antinodes = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != ".":
                find_antinodes_with_harmonics(grid, r, c, antinodes)

    print(f"Part 2: {len(antinodes)}")


if __name__ == "__main__":
    main()
