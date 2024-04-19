from tictactoe import X, O, EMPTY, initial_state, player, actions, terminal_board

def test_player():
	print("Testing player")
	print("--------------")

	def test_player_empty_board():
		"""
		Test player on an empty board
		"""
		print("Testing player on an empty board")

		board = initial_state()
		assert player(board) == X


	def test_player_after_first_movement():
		"""
		Test player after first movement
		"""
		print("Testing player after first movement")

		board = initial_state()
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
	

	test_player_empty_board()
	test_player_after_first_movement()
	test_player_with_terminal_board()
	print("---\n✅ All player tests pass\n\n")


def test_actions():
	print("Testing actions")
	print("---------------")

	def test_actions_empty_board():
		"""
		Test actions on an empty board
		"""
		print("Testing actions on an empty board")

		board = initial_state()
		assert actions(board) == {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}


	def test_actions_after_first_movement():
		"""
		Test actions after the first movement
		"""
		print("Testing actions after the first movement")

		board = initial_state()
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
	
	test_actions_empty_board()
	test_actions_after_first_movement()
	test_actions_with_terminal_board()
	print("---\n✅ All actions tests pass\n\n")


test_player()
test_actions()
print("---\n✅ All tests pass")