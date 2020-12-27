
#Divides game list into rows of 3
def segment_list(lst, n):
	for i in range(0, len(lst), n):
		yield lst[i:i + n]


def pick_marker():
	marker = ''

	while marker != 'X' and marker != 'O':
		marker = input('Player 1 choose X or O: ')

	player1 = marker

	if player1 == 'X':
		player2 = 'O'
	else:
		player2 = 'X'

	return (player1,player2)


def display_board(board):
	print(board[1] + ' | ' + board[2] + ' | ' + board[3])
	print(board[4] + ' | ' + board[5] + ' | ' + board[6])
	print(board[7] + ' | ' + board[8] + ' | ' + board[9])

def position_choice():

	#INITIAL CONDITIONS TO CHECK:
	choice = 'Wrong'
	acceptable_range = range(1,10)
	within_range = False
    
	while choice.isdigit() == False or within_range == False:
        
		choice = input("Pick a position (1-9): ")
        
		#DIGIT CHECK
		if choice.isdigit() == False:
			print("Sorry that is not a digit!")

		#RANGE CHECK
		if choice.isdigit() == True:
			if int(choice) in acceptable_range:
				within_range = True
			else:
				print("Sorry that was not within the acceptable range")
      
	return int(choice)

def replacement_value(board, marker, position):
	user_placement = marker
	board[position] = user_placement
	return board

def check_win(board):
	win = False
	#calling the global player markers into the function
	global p1, p2

	#we need to divide the board into rows, columns, and diagonals
	row_list = list(segment_list(board,3))

	row1 = row_list[0]
	row2 = row_list[1]
	row3 = row_list[2]

	column_list = [ [row1[0],row2[0],row3[0]], [row1[1],row2[1],row3[1]], [row1[2],row2[2],row3[2]] ]

	diagonal_1 = [row1[0], row2[1], row3[2]]
	diagonal_2 = [row3[0], row2[1], row1[2]]

	while win == False:
		#CHECK HORIZONTAL WIN
		for i in range(0, len(row_list)):
			if row_list[i] == [p1]*3:
				win = True
				print("Player#1 won!")
			if row_list[i] == [p2]*3:
				win = True
				print("Player#2 won!")

		#CHECK VERTICAL WIN
		for i in range(0, len(column_list)):
			if column_list[i] == [p1]*3:
				win = True
				print("Player#1 won!")
			if column_list[i] == [p2]*3:
				win = True
				print("Player#2 won!")

		#CHECK DIAGONAL WIN
		if diagonal_1 == [p1]*3:
			win = True
			print("Player#1 won!")
		if diagonal_1 == [p2]*3:
			win = True
			print("Player#2 won!")

		if diagonal_2 == [p1]*3:
			win = True
			print("Player#1 won!")
		if diagonal_2 == [p2]*3:
			win = True
			print("Player#2 won!")
	
	return win

################################
#GAME LOGIC
################################

board = ['']*10
gameon = False

#markers for player 1 and 2 are set equal to tuple returned from pick_marker()
(p1, p2)= pick_marker()

while gameon == False:

	display_board(board)
	position = position_choice()
	board = replacement_value(board, p1 , position)
	display_board(board)

	position = position_choice()
	board = replacement_value(board, p2 , position)
	display_board(board)

	gameon = check_win(board)





