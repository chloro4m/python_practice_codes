#write code that uses it to print the image:
#(looks like 90 degree clockwise rotate to me...)
##..OO.OO..
##.OOOOOOO.
##.OOOOOOO.
##..OOOOO..
##...OOO...
##....O....

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(0, len(grid[0])):
    for j in range (0, len(grid)):
        print(grid[j][i], end='')
    print('\n')
