
import itertools
import sys

OPERATORS = ['*','+']

def get_input_data():
    with open("./inputs/day7_input.txt") as file:
        lines = [line.split() for line in file]
        result = [int(line[0][:-1]) for line in lines]
        values = [[int(element) for element in line[1:]] for line in lines]
        return result, values
    
def is_possible(result, values):
    operators = generate_operators(len(values)-1)
    for op_sequence in operators:
        if evaluate(values, op_sequence) == result:
            return True
        
    return False

def evaluate(values: list[int], op_sequence: list[str]):
    values = list(values)
    op_sequence = list(op_sequence)
    res = values.pop(0) # Get first element

    while True:
        v1 = res
        v2 = values.pop(0)
        operator = op_sequence.pop(0)
        res = apply_op(operator, v1, v2)
        if len(values) == 0:
            break
    return res

def apply_op(op: str, v1 : int, v2: int) -> int:
    if op == '*':
        return v1 * v2
    return v1 + v2
    

def generate_operators(n : int) -> list[list[str]]:
    # For n = 2 it could be ** +* +* ++
    l1 = [list(p) for p in itertools.product(['*','+'],repeat=n)] # This is cheating? Do it with recursion
    l2 = generate_operators_recursively(n)
    return l2

def generate_operators_recursively(n : int):
    return gen_op_rec(n, list([] for _ in range(pow(2,n))))

def gen_op_rec(n: int, l: list[list[str]]):
    length = len(l)
    if n == 0: 
        return l
    op = 0
    for i in range(length):
        l[i].append(OPERATORS[op])
        if i % (pow(2,n) // 2) == 0:
            op = 1 if op == 0 else 0
            
    return gen_op_rec(n-1, l)

def main():
    result, values = get_input_data()
    s = 0

    for result, value in zip(result, values):
        if is_possible(result,value):
            s += result

    print(f"Part 1: {s}")
    # Ans: 12553187650171


if __name__ == "__main__":
    main()