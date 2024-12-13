
def get_input_data() -> list[str]:
    with open("./inputs/day4_input.txt","r") as file:
        return [line.strip() for line in file]
    
def is_after(l2: str, l1: str) -> bool:
    if l1 == "X" and l2 == "M": return True
    if l1 == "M" and l2 == "A": return True
    if l1 == "A" and l2 == "S": return True
    return False

def find_x(rows: list[str], r: int, c: int) -> bool:
    currentChar = rows[r][c]

    if currentChar != "A": return False

    maxLengthRow = len(rows)
    maxLengthCol = len(rows[r])

    if r - 1 < 0 or r + 1 >= maxLengthRow: return False

    if c - 1 < 0 or c + 1 >= maxLengthCol: return False

    if rows[r-1][c-1] == "A" or rows[r+1][c+1] == "A" or rows[r+1][c-1] == "A" or rows[r-1][c+1] == "A":
        return False
    
    if rows[r-1][c-1] == rows[r+1][c+1] or rows[r+1][c-1] == rows[r-1][c+1]:
        return False
    
    if rows[r-1][c-1] == "X" or rows[r+1][c+1] == "X" or rows[r+1][c-1] == "X" or rows[r-1][c+1] == "X":
        return False
    
    return True

def find_x_count(rows: list[str]) -> int:
    count = 0
    for r in range(len(rows)):
        for c in range(len(rows[r])):
            if find_x(rows, r, c):
                count += 1
    return count

# Not my proudest work, could use some refactoring
def main():
    rows = get_input_data()
    # Part 1
    count = 0
    for r in range(len(rows)):
        for c in range(len(rows[r])):
            currentChar = rows[r][c]
  
            if currentChar == "X":
                
                # First check to left
                prev_index = c -1
                while prev_index >= 0:
                    if is_after(rows[r][prev_index], currentChar) and rows[r][prev_index] == "S":
                        count += 1
                        break
                    if is_after(rows[r][prev_index], currentChar):
                        currentChar = rows[r][prev_index]
                        prev_index -= 1
                    else:
                        break
                
                # Check to right
                currentChar = "X"
                next_index = c + 1
                while next_index < len(rows[r]):
                    if is_after(rows[r][next_index], currentChar) and rows[r][next_index] == "S":
                        count += 1
                        break
                    if is_after(rows[r][next_index], currentChar):
                        currentChar = rows[r][next_index]
                        next_index += 1
                    else:
                        break
                # Check above: 
                currentChar = "X"
                prev_row_index = r - 1
                while prev_row_index >= 0:
                    if is_after(rows[prev_row_index][c], currentChar) and rows[prev_row_index][c] == "S":
                        count += 1
                        break
                    if is_after(rows[prev_row_index][c], currentChar):
                        currentChar = rows[prev_row_index][c]
                        prev_row_index -= 1
                    else:
                        break
                # Check below
                currentChar = "X"
                next_row_index = r + 1
                while next_row_index < len(rows):
                    if is_after(rows[next_row_index][c], currentChar) and rows[next_row_index][c] == "S":
                        count += 1
                        break
                    if is_after(rows[next_row_index][c], currentChar):
                        currentChar = rows[next_row_index][c]
                        next_row_index += 1
                    else:
                        break
                # Check diagonally left down
                currentChar = "X"
                next_row_index = r + 1
                next_col_index = c - 1
                while next_row_index < len(rows) and next_col_index >= 0:
                    if is_after(rows[next_row_index][next_col_index], currentChar) and rows[next_row_index][next_col_index] == "S":
                        count += 1
                        break
                    if is_after(rows[next_row_index][next_col_index], currentChar):
                        currentChar = rows[next_row_index][next_col_index]
                        next_row_index += 1
                        next_col_index -= 1
                    else:
                        break
                # Check diagonally left up
                currentChar = "X"
                next_row_index = r - 1
                next_col_index = c - 1
                while next_row_index >= 0 and next_col_index >= 0:
                    if is_after(rows[next_row_index][next_col_index], currentChar) and rows[next_row_index][next_col_index] == "S":
                        count += 1
                        break
                    if is_after(rows[next_row_index][next_col_index], currentChar):
                        currentChar = rows[next_row_index][next_col_index]
                        next_row_index -= 1
                        next_col_index -= 1
                    else:
                        break

                # Check diagonally right down
                currentChar = "X"
                next_row_index = r + 1
                next_col_index = c + 1
                while next_row_index < len(rows) and next_col_index < len(rows[r]):
                    if is_after(rows[next_row_index][next_col_index], currentChar) and rows[next_row_index][next_col_index] == "S":
                        count += 1
                        break
                    if is_after(rows[next_row_index][next_col_index], currentChar):
                        currentChar = rows[next_row_index][next_col_index]
                        next_row_index += 1
                        next_col_index += 1
                    else:
                        break
                # Check diagonally right up
                currentChar = "X"
                next_row_index = r - 1
                next_col_index = c + 1
                while next_row_index >= 0 and next_col_index < len(rows[r]):
                    if is_after(rows[next_row_index][next_col_index], currentChar) and rows[next_row_index][next_col_index] == "S":
                        count += 1
                        break
                    if is_after(rows[next_row_index][next_col_index], currentChar):
                        currentChar = rows[next_row_index][next_col_index]
                        next_row_index -= 1
                        next_col_index += 1
                    else:
                        break
    print(f"Part 1: {count}")


    # Part 2
    print(f"Part 2: {find_x_count(rows)}")

if __name__ == "__main__":
    main()