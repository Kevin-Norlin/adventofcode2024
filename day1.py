


def _get_input():
    # Get the input
   
    list1 = []
    list2 = []
  
    text_file = open("./inputs/day1_input.txt", "r")
    for line in text_file:
        string = line.split() # [elem1, elem2]
        
        list1.append(int(string[0]))
        list2.append(int(string[1]))
        
    return list1, list2

# Part 1

def _pair_up_lists(list1: list[int], list2: list[int]) -> list[tuple[int,int]]:
    return list(zip(sorted(list1),sorted(list2)))
    
    
def _calculate_total_diff(list_of_pairs: list[tuple[int,int]]) -> int:
    return sum(map(lambda pair: abs(pair[0] - pair[1]), list_of_pairs))

def get_total_diff(list1: list[int], list2: list[int]) -> int:
    list_of_pairs = _pair_up_lists(list1,list2)

    return _calculate_total_diff(list_of_pairs)

# Part2

def get_times_present(val: int, input_list: list[int]) -> int:

    return sum(1 for elem in input_list if elem == val)
    

def get_similarity_score(list1 : list[int], list2 : list[int]) -> int:
    return sum(get_times_present(x, list2) * x for x in list1)


def main():
    list1, list2 = _get_input()

    print(f"Task 1: {get_total_diff(list1,list2)}")
    print(f"Task 2: {get_similarity_score(list1,list2)}")

if __name__ == "__main__":
    main()

