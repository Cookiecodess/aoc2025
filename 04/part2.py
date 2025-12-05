filename="input.txt"

curr_removed_coords = []

def is_accessible(x: int, y: int, grid: list[list[str]]) -> bool:
    rolls_around = 0
    for col_diff in range(-1,2):
        for row_diff in range(-1,2):
            if col_diff==0 and row_diff==0:
                continue
            curr_col = x + col_diff 
            curr_row = y + row_diff 
            print('row:',curr_row,'col:',curr_col)
            if curr_col<0 or curr_row<0 or curr_col>=len(grid[0]) or curr_row>=len(grid):
                print('skipped')
                continue
            if grid[curr_row][curr_col] == '@':
                print('is a roll')
                rolls_around+=1
    print('there were',rolls_around,'around it.')
    return rolls_around<4

def count_accessible_rolls(grid: list[list[str]]) -> int:
    accessible=0
    global curr_removed_coords
    curr_removed_coords.clear()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] != '@':
                continue
            if is_accessible(col, row, grid):
                accessible+=1  
                curr_removed_coords.append((row, col))
                #grid[row][col]='x' 
    return accessible 

def update_grid(grid: list[list[str]]) -> None:
    global curr_removed_coords
    for row, col in curr_removed_coords:
        grid[row][col] = "x"

def print_grid(grid: list[list[str]]):
    for row in grid:
        for col in row:
            print(col, end='')
        print('\n',end='')

def get_grid() -> list[list[str]]:
    grid=[]
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            grid.append([chr for chr in line])
    return grid 

def main():
    grid = get_grid()
    total_removed = 0
    #print(is_accessible(2,0,grid))
    #return
    while True:
        newly_removed = count_accessible_rolls(grid)
        if newly_removed == 0:
            break
        total_removed += newly_removed
        update_grid(grid)
        print_grid(grid)
    print(total_removed)



if __name__=='__main__':
    main()
