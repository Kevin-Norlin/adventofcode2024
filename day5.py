
from collections import defaultdict, deque
from functools import cmp_to_key


def get_input_data():
    # Parse the rules and then the page numbers
    with open("./inputs/day5_input.txt", "r") as file:
        lines = [line.split() for line in file]
        rules = []
        page_numbers = []
        i = 0
        while (len(lines[i]) != 0):
            rules.append(lines[i][0].split("|"))
            i += 1
        i += 1
        while (i < len(lines)):
            page_numbers.append(lines[i][0].split(","))
            i += 1
        
        return rules, page_numbers
    
def get_rules(val: str, rules: list[list[str]]):
    before = [rule[0] for rule in rules if rule[1] == val] # Values that should come before val
    after = [rule[1] for rule in rules if rule[0] == val] # Values that should come after val

    return before, after

def breaks_rules(val: str, rules: list[list[str]], page : list[str]) -> bool:
    before, after = get_rules(val, rules)
    index = page.index(val)
    
    breaks_before = any(x in before for x in page[index+1:])
    breaks_after = any(x in after for x in page[:index])

    return breaks_before or breaks_after

def order_correctly(page: list[str], rules) -> list[str]:
    arr = list(page)
    while page_breaks_rules(arr, rules):
        for i in range(len(arr)): 
            before, _ = get_rules(arr[i],rules)
            # Find a before elem and swap places with it - bubblesort
            p1 = i +1 
            while(p1 < len(arr)): 
                if arr[p1] in before:
                    tmp = arr[p1]
                    arr[p1] = arr[i]
                    arr[i] = tmp
                    break
                p1 += 1
    return arr

def page_breaks_rules(page, rules):
    for val in page:
        if breaks_rules(val, rules, page):
            return True
    return False
 
def get_correct_pages(page_numbers):
    rules, _ = get_input_data()
    page_obides = []
    for page in page_numbers:
        obides = True
        for val in page: 
            if breaks_rules(val,rules,page):
                obides = False
                break
        if obides:
            page_obides.append(page)
    return page_obides

def main():

    #Part 1
    rules, page_numbers = get_input_data()
    page_obides = get_correct_pages(page_numbers)
    total = sum(int(page[len(page)//2]) for page in page_obides)
    print(f"Part1: {total}") #4774

    #Part 2
    not_obides_pages = [page for page in page_numbers if page not in page_obides]
    ordered_correctly = [(order_correctly(page,rules)) for page in not_obides_pages]
    total2 = sum(int(page[len(page)// 2]) for page in ordered_correctly)
    print(f"Part2: {total2}") #6004

if __name__ == "__main__":
    main()