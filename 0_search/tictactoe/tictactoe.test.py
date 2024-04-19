from tictactoe import X, O, EMPTY, initial_state, player, actions, result, winner, terminal

def terminal_board():
    return [[X, O, X],
            [O, X, O],
            [X, O, X]]

def test_player():
	print("Testing player")
	print("--------------")

	def test_player_during_game():
		"""
		Test player during game
		"""
		print("Testing player during game")

		board = initial_state()
		assert player(board) == X

		board[0][0] = X
		assert player(board) == O

		board[0][1] = O
		assert player(board) == X

		board[1][0] = X
		assert player(board) == O

		board[1][1] = O
		assert player(board) == X


	def test_player_with_terminal_board():
		"""
		Test player with terminal board
		"""
		print("Testing player with terminal board")
		board = terminal_board()
		assert player(board) == O
	

	test_player_during_game()
	test_player_with_terminal_board()
	print("---\n✅ All player tests pass\n\n")


def test_actions():
	print("Testing actions")
	print("---------------")

	def test_actions_during_game():
		"""
		Test actions during game
		"""
		print("Testing actions during game")

		board = initial_state()
		assert actions(board) == {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}

		board[0][0] = X
		assert actions(board) == {(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}

		board[0][1] = O
		assert actions(board) == {(0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}

		board[0][2] = X
		assert actions(board) == {(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}

		board[2][2] = O
		assert actions(board) == {(1, 0), (1, 1), (1, 2), (2, 0), (2, 1)}


	def test_actions_with_terminal_board():
		"""
		Test actions with terminal board
		"""
		print("Testing actions with terminal board")
		board = terminal_board()
		assert actions(board) == set()
	
	test_actions_during_game()
	test_actions_with_terminal_board()
	print("---\n✅ All actions tests pass\n\n")


def test_result():
	print("Testing result")
	print("--------------")

	def test_result_during_game():
		"""
		Test result during game
		"""
		print("Testing result during game")

		board = initial_state()
		new_board = result(board, (0, 0))
		assert new_board == [[X, EMPTY, EMPTY],
							 [EMPTY, EMPTY, EMPTY],
							 [EMPTY, EMPTY, EMPTY]]

		new_board = result(board, (2, 2))
		assert new_board == [[EMPTY, EMPTY, EMPTY],
							 [EMPTY, EMPTY, EMPTY],
							 [EMPTY, EMPTY, X]]
		
		new_board = result(new_board, (1, 1))
		assert new_board == [[EMPTY, EMPTY, EMPTY],
							 [EMPTY, O, EMPTY],
							 [EMPTY, EMPTY, X]]
		

	def test_result_with_terminal_board():
		"""
		Test result with terminal board
		"""
		print("Testing result with terminal board")

		board = terminal_board()
		try:
			result(board, (0, 0))
		except Exception as e:
			assert str(e) == "Game is over"
		
		

	test_result_during_game()
	test_result_with_terminal_board()
	print("---\n✅ All result tests pass\n\n")


def test_winner():
	print("Testing winner")
	print("--------------")

	def test_winner_during_game():
		"""
		Test winner during game
		"""
		print("Testing winner during game")

		board = initial_state()
		assert winner(board) == None

		board[0][0] = X
		assert winner(board) == None

		board[0][1] = X
		assert winner(board) == None

		board[0][2] = X
		assert winner(board) == X

		board = initial_state()
		board[0][0] = O
		board[1][0] = O
		board[2][0] = O
		assert winner(board) == O

		board = initial_state()
		board[0][0] = X
		board[1][1] = X
		board[2][2] = X
		assert winner(board) == X

		board = initial_state()
		board[0][2] = O
		board[1][1] = O
		board[2][0] = O
		assert winner(board) == O

		board = initial_state()
		board[0][1] = X
		board[1][1] = X
		board[2][1] = X
		assert winner(board) == X

		board = initial_state()
		board[0][2] = O
		board[1][2] = O
		board[2][2] = O
		assert winner(board) == O
		

	def test_winner_with_terminal_board():
		"""
		Test winner with terminal board
		"""
		print("Testing winner with terminal board")
		board = [[X, O, X],
				 [O, X, O],
				 [O, X, O]]
		assert winner(board) == None

	test_winner_during_game()
	test_winner_with_terminal_board()
	print("---\n✅ All winner tests pass\n\n")


def test_terminal():
	print("Testing terminal")
	print("--------------")

	def test_terminal_during_game():
		"""
		Test terminal during game
		"""
		print("Testing terminal during game")

		board = initial_state()
		assert terminal(board) == False

		board[0][0] = X
		assert terminal(board) == False

		board[0][1] = X
		assert terminal(board) == False

		board[0][2] = X
		assert terminal(board) == True

		board = initial_state()
		board[0][0] = O
		board[1][0] = O
		board[2][0] = O
		assert terminal(board) == True

		board = initial_state()
		board[0][0] = X
		board[1][1] = X
		board[2][2] = X
		assert terminal(board) == True

		board = initial_state()
		board[0][2] = O
		board[1][1] = O
		board[2][0] = O
		assert terminal(board) == True

		board = initial_state()
		board[0][1] = X
		board[1][1] = X
		board[2][1] = X
		assert terminal(board) == True

		board = initial_state()
		board[0][2] = O
		board[1][2] = O
		board[2][2] = O
		assert terminal(board) == True
		

	def test_terminal_with_terminal_board():
		"""
		Test terminal with terminal board
		"""
		print("Testing terminal with terminal board")
		board = terminal_board()
		assert terminal(board) == True

	test_terminal_during_game()
	test_terminal_with_terminal_board()
	print("---\n✅ All terminal tests pass\n\n")


test_player()
test_actions()
test_result()
test_winner()
test_terminal()

print("---\n✅ All tests pass")