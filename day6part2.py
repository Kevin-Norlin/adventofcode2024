
import copy

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
        area[pos_y][pos_x] = get_rotation(area[pos_y][pos_x]) # Rotate arrow (direction)
        return (pos_y, pos_x), 0 # Keep old pos with rotation, moved 0 steps
    
    # Just move 1 in the direction
    moved_count = 0 if area[next_pos_y][next_pos_x] == "X" else 1
    area[next_pos_y][next_pos_x] = direction # Move to next pos
    area[pos_y][pos_x] = "X"
    
    return (next_pos_y, next_pos_x), moved_count

def main():
    # Part 1
    area = get_input_data()
    pos = get_start_pos(area)
    c = 1
    while True:
        pos, steps_moved = move(area, pos)
        if (steps_moved == -1):
            break
        c += steps_moved
        
    print(f"Part 1: {c}")
    # Ans: 4374

    # Part 2
    area = get_input_data()
    pos = get_start_pos(area)
    obstacle_positions = set()
    spawn_point = pos
    visited_positions_with_direction = set()
    c = 0
    itt = 0
    while True:
        # Move guard like regular
        if itt != 0:
            pos, x = move(area, pos)
            if x == -1:
                break
        py,px = pos
        dir = area[py][px]
        visited_positions_with_direction.add((pos, dir)) # Add all positions with its corresponding direction to visited
        
        # Now check for potential cycles
        ghost_pos = pos
        ghost_area = copy.deepcopy(area) # This is not memory efficient
        ghost_dir = ghost_area[ghost_pos[0]][ghost_pos[1]]
        
        # Check if obstacle has already been placed here
        obstacle_pos = get_next_pos(ghost_pos,ghost_dir)
        
        if obstacle_pos in obstacle_positions or obstacle_pos == spawn_point:
            continue
        if obstacle_pos[0] < 0 or obstacle_pos[0] > len(area) -1  or obstacle_pos[1] < 0 or obstacle_pos[1] > len(area) -1 :
            continue
        if ghost_area[obstacle_pos[0]][obstacle_pos[1]] == "#":
            continue
        
        obstacle_positions.add(obstacle_pos)
        ghost_area[obstacle_pos[0]][obstacle_pos[1]] = "#"

        ghost_visited_positions = set()

        # Check if the obstacle placement caused a loop
        while True:
            ghost_pos, x = move(ghost_area, ghost_pos)
            
            if x == -1:
                break

            ghost_dir = ghost_area[ghost_pos[0]][ghost_pos[1]]

            # Loop detected!
            if (ghost_pos, ghost_dir) in visited_positions_with_direction or (ghost_pos, ghost_dir) in ghost_visited_positions:
                c += 1
                break
            
            ghost_visited_positions.add((ghost_pos, ghost_dir))
        
        itt += 1
        
    print(f"Part 2: {c}")
    # Ans 1705

if __name__ == "__main__":
    main()