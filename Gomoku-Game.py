N, M = 15, 15
a_row = 5
n_players = 2
marks = ['X', 'O']
grid = []

#This function prints the grid of Gomoku as the game progresses
def print_grid():
    for i in range(n_players):
        print('Player %d: %c  ' % (i+1, marks[i]), end='')
        if i < n_players-1:
            print('vs  ', end='')
    print()
    print('--' + '---' * M + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(M):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        print('--' + '---' * M + '--')
#This function checks the existence of any winning row
def check_rows(grid):
    for row in range(N):
        for col in range(M-(a_row-1)):
            for i in range(col+1,col+a_row):
                if grid[row][col]==grid[row][i] and grid[row][col] in marks :
                    continue
                else:
                    break
            else:
                return True
    return False         
#This function checks the existence of any winning column
def check_cols(grid):
    for col in range(M):
        for row in range(N-(a_row-1)):
            for i in range(row+1,row+a_row):
                if grid[row][col]==grid[i][col] and grid[row][col] in marks :
                    continue
                else:
                    break
            else:
                return True
    return False 
#This function checks the existence of any winning diagonal
def check_diags(grid):
    for row in range(N-(a_row-1)):
        for col in range(M-(a_row-1)):
            j = col + 1
            for i in range(row+1,row+a_row):
                if grid[row][col] == grid[i][j] and grid[row][col] in marks :
                    j+=1
                    continue
                else:
                    break
            else:
                return True

    for row in range(N-1,N-(N-a_row),-1):
        for col in range(M-(a_row-1)):
            j = col + 1
            for i in range(row-1,row-a_row,-1):
                if grid[row][col] == grid[i][j] and grid[row][col] in marks :
                    j+=1
                    continue
                else:
                    break
            else:
                return True
    return False

#This function checks if the game has a win state or not
def check_win():
    if check_rows(grid) or check_cols(grid) or check_diags(grid):
        return True
    else:
        return False
#This function makes a temporary copy from grid and fill the spaces with specific mark
def list_try(mark):
    temp=[]
    for row in range(N):
        l = []
        for col in range(M):
            if grid[row][col] == " ":
                l.append(mark)
            else:
                l.append(grid[row][col])
        temp.append(l)
    return temp
#This function checks if the game has a tie state or not for the given mark
def check_tie_player(mark):
    temp = list_try(mark)
    if check_rows(temp) or check_cols(temp) or check_diags(temp):
        return False
    else:
        return True

#This function checks if the game has a tie state or not
def check_tie():
    all_tie = True
    for mark in marks:
        if not check_tie_player(mark):
            all_tie = False
    return all_tie
	
#This function checks if given cell is empty or not 
def check_empty(i, j):
    if grid[i][j] == " ":
        return True
    else : 
        return False

#This function checks if given position is valid or not 
def check_valid_position(i, j):
    if 0<=i<N and 0<=j<M :
        return True
    else:
        return False

#This function sets the given mark to the given cell
def set_cell(i, j, mark):
    grid[i][j] = mark

#This function clears the game structures
def grid_clear():
    grid.clear()
    for i in range(N):
        l = [" "]*M
        grid.append(l)

#This function reads a valid position input
def read_input():
    i, j = map(int, input('Enter the row index and column index: ').split())
    while not check_valid_position(i, j) or not check_empty(i, j):
        i, j = map(int, input('Enter a valid row index and a valid column index: ').split())
    return i, j


#MAIN FUNCTION
def play_game():
    print("Gomoku Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Read an input position from the player
        print('Player %s is playing now' % marks[player])
        i, j = read_input()
        #Set the player mark in the input position
        set_cell(i, j, marks[player])
        #Check if the grid has a win state
        if check_win():
            #Prints the grid
            print_grid()
            #Announcement of the final statement
            print('Congrats, Player %s is won!' % marks[player])
            break
        #Check if the grid has a tie state
        if check_tie():
            #Prints the grid
            print_grid()
            #Announcement of the final statement
            print("Woah! That's a tie!")
            break		
        #Player number changes after each turn
        player = (player + 1) % n_players


while True:
	grid_clear()
	play_game()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		break
