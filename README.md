# My projects from CS50's Introduction to AI with Python

> NOTE: I hope you use this to learn yourself and not just to copy the code to pass the course. They will know and you'll only be fooling yourself.

## 0. Search

### Degrees

It's an implementation of the [Six degrees of Kevin Bacon](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon) with a simple Breadth-first Search algorithm.

You can find it in the folder `/0_search/degrees`. For this project I only coded two functions inside the `degrees.py` file:

- `shortest_path()`: this is the only function in the file that you can modify, and it's where you implement the algorithm. But I also created a helpr function,
- `generate_solution()`: this function takes the solution node as a parameter and builds the array with the full path.

### Tic-Tac-Toe

It will be an implementation of Tic-Tac-Toe where you play agains a Minimax AI.

**Currently working on this**

It's in the folder `/0_search/tictactoe`. For this project there are a lot of functions to code inside the `tictactoe.py` file:

- `player(board)`: this function determines which player will play next, depending on the `board`'s state.
- `actions(board)`: this returns all possible actions for the next player on the current `board`.
- `result(board, action)`: returns the result of playing `action` on `board`.
- `winner(board)`: determines the winner of the `board`, if any.
- `terminal(board)`: returns `True` if the game is over, `False` otherwise.
- `utility(board)`: returns `1` if **X** has won the game, `-1` if **O** has won, `0` otherwise.
- `minimax(board)`: returns the optimal action for the current player on the `board`.

I have also added the following utility functions to the `tictactoe.py` file:

- `flat(list)`: flattens a two-dimensional array into a simple array.
- `terminal_board()`: returns a full board.

Additionally, I have created a `tictactoe.test.py` where I'm creating unit tests for the functions that I have to implement. This allows me to progress without having to run the game (which will crash until all the functions are implemented).