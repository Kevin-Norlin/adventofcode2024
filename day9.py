
def get_input_string() -> list[str]:
    with open("./inputs/day9_input.txt","r") as file:
        return [list(line) for line in file][0]
    
def convert_to_dot_rep(arr: list[str]) -> list[str]:
    dot_form = []
    for i, elem in enumerate(arr):
        if i % 2 == 0:
            dot_form += [(i//2)]* int(elem)
        else:
            dot_form += ["."]* int(elem)
    return dot_form

def get_slot_with_space(dot_form: list[str], file_size: int) -> int: 
    # Find a slot that is min the file size
    for i, elem in enumerate(dot_form):
        if elem == ".":
            ptr = i
            acc = 0
            while True:
                if ptr > len(dot_form) - 1 or dot_form[ptr] != ".":
                    i += acc
                    break
                acc += 1
                ptr += 1
                if acc >= file_size:
                    return i
    return -1 # No slot found

def get_file_size(i : int, dot_form: list[str]):
    acc = 1
    elem = dot_form[i]
    j = i -1
    while j >= 0 and dot_form[j] == elem:
        acc += 1
        j -= 1

    return acc

def main():
    
    # Part 1
    string = get_input_string()
    dot_form = convert_to_dot_rep(string)

    pl, ph = 0, len(dot_form) -1

    while True:
        while pl < len(dot_form) and dot_form[pl] != "." : pl += 1
        while  ph >= 0 and dot_form[ph] == ".": ph -= 1
        if pl >= ph:
            break
        # Swap
        dot_form[pl], dot_form[ph] = dot_form[ph], dot_form[pl]

    acc = 0
    for i, elem in enumerate(dot_form):
        if elem == ".": 
            break
        acc += i * elem
    
    print(acc)
    # Ans: 6385338159127

    # Part 2
    string = get_input_string()
    dot_form = convert_to_dot_rep(string)
   
    i = len(dot_form) -1
    while i >= 0:
        while i >= 0 and dot_form[i] == ".": i -= 1
        fs = get_file_size(i, dot_form)
        slot = get_slot_with_space(dot_form, fs)
        if slot == -1 or slot >= i:
            i -= fs
            continue

        # Swap the whole file
        file_ptr = i
        for j in range(fs):
            dot_form[slot], dot_form[file_ptr] = dot_form[file_ptr], dot_form[slot]
            slot += 1
            file_ptr -= 1
        i -= fs

    acc = 0
    for i, elem in enumerate(dot_form):
        if elem == ".": 
            continue
        acc += i * elem

    print(acc)
    # Ans: 6415163624282

if __name__ == "__main__":
    main()