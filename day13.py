
from collections import defaultdict
import time

A_COST = 3
B_COST = 1
MAX_PRESS = 100
PART_2_MULTIPLIER = 10000000000000

def get_input():
    with open("./inputs/day13_input.txt", "r") as file:
        lines = [line.strip() for line in file]

        # dict key: machine num, val: list with Button A (x,y), Button B (x,y), Result: (x,y)
        # e.g. 0 : [(x,y),(x2,y2),(x3,y3)]
        key = 0
        machines = defaultdict(list)
        for line in lines:
            if len(line) == 0:
                key += 1
                continue
            line = line.split()
            if line[0] == "Prize:":
                machines[key].append((int(line[1][2:].replace(",","")),int(line[2][2:])))
            else:
                machines[key].append((int(line[2][2:].replace(",","")),int(line[3][2:])))
                

        return machines

def find_cheapest_combination(machine : list[tuple[int,int]]) -> int:
    a = machine[0]
    a_x,a_y = a
    b = machine[1]
    b_x,b_y = b
    target = machine[2]
    target_x, target_y = target
    
    min_cost = float('inf')
    for a_pressed in range(MAX_PRESS):
        for b_pressed in range(MAX_PRESS):
            x_sum = a_x * a_pressed + b_x * b_pressed
            y_sum = a_y * a_pressed + b_y * b_pressed
            if x_sum == target_x and y_sum == target_y:
                tokens =  a_pressed * A_COST + b_pressed * B_COST
                if tokens < min_cost:
                    min_cost = tokens

    if min_cost == float('inf'):
        return 0 # Not possible to win the price
    
    return min_cost


# This will have to be a bit quicker, binary search???+
def find_cheapest_combination_p2(machine: list[tuple[int,int]]): 
    a = machine[0]
    a_x,a_y = a
    b = machine[1]
    b_x,b_y = b
    target = machine[2]
    target_x, target_y = target
    target_x, target_y = PART_2_MULTIPLIER + target_x, target_y + PART_2_MULTIPLIER
    # We still need to find all possible combinations of A and B that meets the target and then choose the cheapest one
    min_cost = float('inf')
    max_a_bound = max(target_x // a_x, target_y // a_y)
    max_b_bound = max(target_x // b_x, target_y // b_y)
    print(f"Doing {max_a_bound * max_b_bound} itterations")
    for a_pressed in range(max_a_bound):
        for b_pressed in range(max_b_bound):
            
            x_sum = a_x * a_pressed + b_x * b_pressed
            y_sum = a_y * a_pressed + b_y * b_pressed
            
            if x_sum == target_x and y_sum == target_y:
                tokens =  a_pressed * A_COST + b_pressed * B_COST
                if tokens < min_cost:
                    min_cost = tokens

    if min_cost == float('inf'):
        return 0 # Not possible to win the price
    print("done with one")
    return min_cost
    
    
    
def main():
    machines = get_input() # Tuple1 : x,y for A, Tuple2: x,y for B, Tuple 3: target
    start = time.time()
    fewest_tokens = sum(map(find_cheapest_combination_p2, machines.values()))
    end = time.time()
    print(end - start)
    print(f"Part 1: {fewest_tokens}")

   
if __name__ == "__main__":
    main()