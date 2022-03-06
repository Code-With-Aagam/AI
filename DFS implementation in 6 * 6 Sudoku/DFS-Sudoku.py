N = 6
def printing(arr):
    print("The Solution of this Sudoku is:")
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()

def isSafe(grid, row, col, num):
   

    for x in range(6):
        if grid[row][x] == num:
            return False
 
   
    for x in range(6):
        if grid[x][col] == num:
            return False
 
#check same num in square

    startRow = row - row % 2
    startCol = col - col % 3
    for i in range(2):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 

def solveSudoku(grid, row, col):
   

    if (row == N - 1 and col == N):
        return True
       
    #go to next row
    if col == N:
        row += 1
        col = 0
 
   
    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)
    for num in range(1, N + 1, 1):
       
        
        # move to next column
        if isSafe(grid, row, col, num):
           
           
            grid[row][col] = num
 
            
            if solveSudoku(grid, row, col + 1):
                return True #avoid backtrack
 
        #number cannot be put into this box
        grid[row][col] = 0
    return False
 
print("Enter grid:")
grid =[]
for i in range(6):
    r=list(map(int,input().split()))
    grid.append(r)
 
if (solveSudoku(grid, 0, 0)):
    printing(grid)
else:
    print("Please check grid")
