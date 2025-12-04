f = open('day4_input.txt')
grid = f.read().split('\n')

number_of_rows = len(grid)
number_of_columns = len(grid[0])

grid_copy = grid
#i = rows
#j = columns

accessible_rolls = 0

for i,row in enumerate(grid):

    for j,column in enumerate(row):
        
        individual_count=0
        #if i,j coord is a roll itself, check for adjacent numbers - check all 8 combinations of [i-1][j-1], [i-1][j], [i-1][j+1], [i][j-1], [i][j+1],etc

        if grid[i][j] == '@':
            #row above
            if i != 0:
                if j != 0:
                    if grid[i-1][j-1] == '@':
                        individual_count+=1

                if grid[i-1][j] == '@':
                    individual_count+=1

                if j < number_of_columns-1:
                    if grid[i-1][j+1] == '@':
                        individual_count+=1

            #row of
            if j != 0:
                if grid[i][j-1] == '@':
                    individual_count+=1

            if j < number_of_columns-1:
                if grid[i][j+1] == '@':
                    individual_count+=1

            #row below
            if i < number_of_rows-1:
                if j != 0:
                    if grid[i+1][j-1] == '@':
                        individual_count+=1

                if grid[i+1][j] == '@':
                    individual_count+=1

                if j < number_of_columns-1:
                    if grid[i+1][j+1] == '@':
                        individual_count+=1
            
            if individual_count < 4:
                accessible_rolls+=1

print(accessible_rolls)

    