board = [
	['O', 'O', 'O'],
	[' ', 'X', 'X'],
	[' ', 'X', ' ']
]

def display_board():
	print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}")
	print("-+-+-")
	print(f"{board[1][0]}|{board[1][1]}|{board[1][2]}")
	print("-+-+-")
	print(f"{board[2][0]}|{board[2][1]}|{board[2][2]}")
def player_input(player) 
    turn = 'X'
    count = 0


	words = input("Write a sequence of words separated by comas: ")
words_list = words.split(",")
words_list.sort()


print(f"The sorted order is: {words_list}")