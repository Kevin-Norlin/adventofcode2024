
import copy
import sys
import time


DOWN = 'v'
UP = '^'
LEFT = '<'
RIGHT = '>'
OBSTACLE = '#'
DOT = '.'

def get_input_data() -> list[list[str]]:
    with open("./inputs/day6_input.txt","r") as file:
        area = [list(line.strip()) for line in file]
        return area

def get_start_pos(area):
    for i in range(len(area)):
        for j in range(len(area)):
            if area[i][j] == '^':
                return i, j
         
def get_next_pos(current_pos : tuple[int], cDir: str) -> tuple[int]:
    cPy, cPx = current_pos
    row_change = 1 if cDir == DOWN else -1 if cDir == UP else 0
    col_change = 1 if cDir == RIGHT else -1 if cDir == LEFT else 0
    nPy, nPx = (cPy + row_change, cPx + col_change)
    return nPy, nPx

def get_rotation(val: str) -> str:
    if val == DOWN: return LEFT
    if val == LEFT: return UP
    if val == UP: return RIGHT
    if val == RIGHT: return DOWN

def is_in_bounds(area, pos):
    l = len(area)
    y,x = pos

    return y >= 0 and y < l and x >= 0 and x < l
 
def move(area, pos: tuple[int]): 
    pos_y, pos_x = pos
    # Get next position 
    direction = area[pos_y][pos_x]
    next_pos_y, next_pos_x = get_next_pos(pos,direction)

    # Check if the position is valid or out of bounds
    if not is_in_bounds(area,(next_pos_y,next_pos_x)):
        return (), -1
    
    # Check if there is a obstruction
    if area[next_pos_y][next_pos_x] == "#":
        area[pos_y][pos_x] = get_rotation(area[pos_y][pos_x])
        return (pos_y, pos_x), 0 
    
    area[next_pos_y][next_pos_x] = direction # Move to next pos
    
    return (next_pos_y, next_pos_x), 1

def check_loop(area, pos) -> int:
    visited_positions = set()
    visited_positions.add((pos, area[pos[0]][pos[1]]))
    
    while True:
        pos, x = move(area,pos)
        if x == -1:
            return 0
        if (pos, area[pos[0]][pos[1]]) in visited_positions:
            return 1
        visited_positions.add((pos, area[pos[0]][pos[1]]))

    
def main():
    # Part 2 - This is a very bad brute force solution, takes 90 seconds...
    # Check the other for a better solution
    start_time = time.perf_counter()
    area = get_input_data()
    pos = get_start_pos(area)
    acc = 0
    for i in range(len(area)):
        for j in range(len(area[i])):
            if area[i][j] == "#" or (i,j) == pos:
                continue
            tmp_area = copy.deepcopy(area)
            tmp_area[i][j] = "#"
            acc += check_loop(tmp_area, pos)
    end_time = time.perf_counter()
    print(f"Done in {end_time - start_time}s, with ans {acc}")

    print(acc)
    # Ans: 1705 

if __name__ == "__main__":
    main()