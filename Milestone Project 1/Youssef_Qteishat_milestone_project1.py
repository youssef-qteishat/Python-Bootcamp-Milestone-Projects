#Divides game list into rows of 3
def segment_list(lst, n):
	for i in range(1, len(lst), n):
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
	print('{b1:1} | {b2:1} | {b3:1}'.format(b1=board[1],b2=board[2],b3=board[3]))
	print('---------')
	print('{b4:1} | {b5:1} | {b6:1}'.format(b4=board[4],b5=board[5],b6=board[6]))
	print('---------')
	print('{b7:1} | {b8:1} | {b9:1}'.format(b7=board[7],b8=board[8],b9=board[9]))
	print(" ")

def space_check(board,position):
	return board[position] == ''

def full_board_check(board):
	for i in range(1,10):
		if space_check(board,i) == True:
			return False
	else:
		return True

def position_choice():

	#INITIAL CONDITIONS TO CHECK:
	choice = 'Wrong'
	acceptable_range = range(1,10)
	within_range = False
    
	while choice.isdigit() == False or within_range == False or not space_check(board,int(choice)):
        
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
		#SPACE CHECK
		if space_check(board,int(choice)) != True:
			print('Sorry, position is occupied. Try another')
      
	return int(choice)

def replacement_value(board, marker, position):
	user_placement = marker
	board[position] = user_placement
	return board

def win_check(board,player_marker):
	player_win = False
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

	while player_win == False:
		#CHECK HORIZONTAL WIN
		for i in range(0, len(row_list)):
			if row_list[i] == [player_marker]*3:
				player_win = True
			else:
				pass

		#CHECK VERTICAL WIN
		for i in range(0, len(column_list)):
			if column_list[i] == [player_marker]*3:
				player_win = True
			else:
				pass

		#CHECK DIAGONAL WIN
		if diagonal_1 == [player_marker]*3:
			player_win = True
		else:
			pass

		if diagonal_2 == [player_marker]*3:
			player_win = True
		else:
			pass

		#if either players win, game ends
		if player_win == True:
			win = True
			return win
		else:
			win = False
			return win

################################
#GAME LOGIC
################################

board = ['']*10

#markers for player 1 and 2 are set equal to tuple returned from pick_marker()
(p1, p2)= pick_marker()
while full_board_check(board) == False or win_check(board,p1) == False or win_check(board,p2):

	#player 1
	display_board(board)
	position = position_choice()
	replacement_value(board, p1, position)
	display_board(board)

	if win_check(board, p1) == True:
		print('Winner: Player 1')
		break
	else:
		if full_board_check(board) == True:
			print('Tie!')
			break
		else:
			pass

	#player 2
	position = position_choice()
	replacement_value(board, p2, position)
	display_board(board)

	if win_check(board, p2) == True:
		print('Winner: Player 2')
		break
	else:
		if full_board_check(board) == True:
			print('Tie!')
		else:
			pass
