
# Rules: 
# * r1: stone == 0 --> replace by 1
# * r2: even digits, e.g. 10 or 1024 then insert 2 stones at that pos: 1 and 0 or 10 and 24
# * r3: else multiply by 2024
# order matters
# 1000 split --> 10 and 0

import time

memo = {} # Used for memoization to optimize recursion

def get_sequence() -> list[str]:
    with open("./inputs/day11_input.txt","r") as file:
        return [line.split() for line in file][0]
    
def apply_rules(stones: list[str], i: int) -> int:
    if stones[i] == '0':
        stones[i] = '1'
        return 1 
    if len(stones[i]) % 2 == 0:
        val = stones[i]
        stones[i] = val[:len(val) // 2]
        stones.insert(i +1, str(int(val[len(val) //2:]))) # Including removing trailing zeroes
        return 2
    stones[i] = str(int(stones[i]) * 2024)
    return 1

def blink(stones):
    i = 0
    # Blink once
    while True:
        i += apply_rules(stones, i)
        if i > len(stones) -1:
            break 

def calc_stones_rec(n, val):
    if n == 0:
        return 0
    
    if val == 0:
        return 0 + calc_stones_rec(n-1,1)
    
    if len(str(val)) % 2 == 0:
        # Split val
        string = str(val)
        s1 = int(string[:len(string) // 2])
        s2 = int(string[len(string) //2:])
        return 1 + calc_stones_rec(n-1, s1) + calc_stones_rec(n-1, s2)
    else:
        return 0 + calc_stones_rec(n-1, val * 2024)

def calc_stones_rec_acc(n, val,acc):
    if n == 0:
        return acc
    
    if val == 0:
        return calc_stones_rec_acc(n-1,1, acc)
    
    if len(str(val)) % 2 == 0:
        # Split val
        string = str(val)
        s1 = int(string[:len(string) // 2])
        s2 = int(string[len(string) //2:])
        return calc_stones_rec_acc(n-1, s1, acc + 1) + calc_stones_rec_acc(n-1, s2, acc + 1)
    else:
        return calc_stones_rec_acc(n-1, val * 2024, acc)
    
# This was the only viable solution
def calc_stones_rec_memo(n, val):
    if n == 0:
        return 0
    
    if (n,val) in memo:
        return memo[(n,val)]
    
    if val == 0:
        memo[(n,val)] = 0 + calc_stones_rec_memo(n-1,1)
        return memo[(n,val)]
        
    if len(str(val)) % 2 == 0:
        # Split val
        string = str(val)
        s1 = int(string[:len(string) // 2])
        s2 = int(string[len(string) //2:])
        memo[(n,val)] = 1 + calc_stones_rec_memo(n-1, s1) + calc_stones_rec_memo(n-1, s2)
    else:
        memo[(n,val)] = 0 + calc_stones_rec_memo(n-1, val * 2024)

    return memo[(n,val)]
      
def main():

    # Part 1
    stones = get_sequence()
    blink_count = 25
    start = time.time()
    for _ in range(blink_count):
        blink(stones)
    
    print(f"Part 1: {len(stones)}")
    print(f"Took {time.time()- start}")
    #Ans: 199982

    # Part 2
    # For this part we need a more efficient solution, 
    # Every time a elemt reaches 0 it does this: -> 1 -> 2024 -> split, so it incs by 1 in in 3 itterations, 0 + 0 + 2
    # After that :
    #               20 -> split
    #                           2 -> 4048 -> split
    #                                               40 -> split
    #                                                           4 -> 8096 -> split
    #                                                                               80 -> split
    #                                                                                           8 -> mul it again
    #                                                                                           0 -> does 0 itt again
    #                                                                               84
    #                                                           0 -> does 0 itt again
    #                                               48
    #                           0 does zero itt again
    #               24 -> split
    #                           2 -> 4048 -> split 
    #                                            40 -> split
    #                                                       4 -> mul
    #                                                       0 -> zero itt again
    #                                            48
    #                           4
    #                   
    # So: +2, +0, +2, +2, +0, +2, +2, +0.... for 1 branch, then for each new child it spawns that child will do: +2, +0, +2, +2, +0 ..... 2
    # Recursion 
    blink_count = 75
    start = time.time()
    ints = list(map(int, get_sequence()))
    length = len(ints)
    for num in ints: 
        length += calc_stones_rec_memo(blink_count,num) 

    print(f"Part 2: {length}")
    print(f"Took {time.time()- start}")
    #Ans: 237149922829154

if __name__ == "__main__":
    main()
