
"""
Levels are safe if:
    - All are levels are INCREASING or DECREASING
    - Any adjacent levels differs by [1,3]
"""

def get_input_data():
    text_file = open("./inputs/day2_input.txt","r")
    reports = list(map(lambda line: list(map(lambda val: int(val),line)), [line.split() for line in text_file]))
    return reports

# Part 1
def check_safe(values : list[int]) -> bool:
    valid_ranges = {-3,-2,-1,1,2,3}
    firstVal = values[0]
    prevVal = values[1]
    if firstVal - prevVal not in valid_ranges: 
        return False
    increasing = firstVal < prevVal
    valid_ranges = {1,2,3} if increasing else {-1,-2,-3} 

    for i in range(2,len(values)):
        if values[i] - prevVal not in valid_ranges:
            return False
        prevVal = values[i]
    
    return True

def check_safe_v2(values : list[int]) -> bool:
    if len(values) < 2:
        return True  # Trivial case with fewer than 2 values
    
    valid_ranges = {-3, -2, -1, 1, 2, 3}
    
    # Compare the first two values
    if values[1] - values[0] not in valid_ranges:
        return False

    # Determine if the sequence is increasing or decreasing
    increasing = values[0] < values[1]
    valid_ranges = {1, 2, 3} if increasing else {-1, -2, -3}
    
    # Iterate over pairs of adjacent values and check differences
    return all(
        (b - a in valid_ranges)
        for a, b in zip(values, values[1:])
    )


# Part 2
def possible_to_make_safe(values: list[int]) -> bool:
    # Just itterate through removing one value for each index, and check if has become safe
    for i in range(len(values)): 
        check = list(values)
        check.pop(i)
        if check_safe(check):
            return True
        
    return False

def main():

    reports = get_input_data()
    totalCount = sum(1 for elem in reports if check_safe(elem))
    
    unsafe_reports = [elem for elem in reports if not check_safe(elem)]
    dampened_reports_count = sum(1 for elem in unsafe_reports if possible_to_make_safe(elem))
    
    print(f"Unsafe reports: {len(unsafe_reports)}")
    print(f"Dampened reports: {dampened_reports_count}")
    print(f"Part 1: {totalCount}")
    print(f"Part 2: {totalCount + dampened_reports_count}")

    
if __name__ == "__main__":
    main()
