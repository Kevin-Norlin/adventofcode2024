import re

def get_input_data() -> str: 
    text_file = open("./inputs/day3_input.txt", "r")
    string ="".join(line for line in text_file)
    return string

def main():
    text = get_input_data()
    # Part 1
    mul_operations = re.findall(r'mul\(\d{1,3},\d{1,3}\)', text)
    digitExtractionPattern = r'\d{1,3},\d{1,3}'
    total_sum = sum(list(map(lambda expr: int(re.findall(digitExtractionPattern, expr)[0].split(",")[0]) * int(re.findall(digitExtractionPattern, expr)[0].split(",")[1]) , mul_operations)))
    print(f"Part 1: {total_sum}")

    # Part 2
    all_ops = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', text)

    mul_enabled = True 
    s = 0
    for expr in all_ops: 
        if "do()" in expr:
            mul_enabled = True
        elif "don't()" in expr: 
            mul_enabled = False
        elif mul_enabled:
            numbers = re.findall(digitExtractionPattern, expr)[0].split(",")
            s += int(numbers[0]) * int(numbers[1])
           
    print(f"Part 2: {s}")

if __name__ == "__main__":
    main()