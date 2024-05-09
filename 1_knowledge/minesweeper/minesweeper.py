import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(sorted(cells))
        self.count = count
        self.safes = []
        self.mines = []

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"
    
    def __hash__(self) -> int:
        return hash(str(self))

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        return self.mines

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        return self.safes

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.mines.append(cell)
            self.cells.remove(cell)

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.safes.append(cell)
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        """ self.counts = []
        for i in range(height):
            self.counts.append([-1,-1,-1]) """

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = set()

    def add_sentence(self, sentence):
        if sentence not in self.knowledge:
            self.knowledge.add(sentence)

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        for sentence in self.knowledge:
            if cell in sentence.cells and cell not in sentence.mines and cell not in self.moves_made:
                self.mines.add(cell)
                sentence.mark_mine(cell)

                if len(sentence.cells) == 1:
                    self.mark_safe(list(sentence.cells)[0])

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        for sentence in self.knowledge:
            if cell in sentence.cells and cell not in sentence.safes and cell not in self.moves_made:
                self.safes.add(cell)
                sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made ✅
            2) mark the cell as safe ✅
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count` ✅
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # Add the cell to the set of moves made
        self.moves_made.add(cell)

        # Add the count to be able to print the board
        (x, y) = cell
        #self.counts[x][y] = count

        #self.print_board()

        # Remove cell from any sentences
        for sentence in self.knowledge:
            if cell in sentence.cells:
                sentence.cells.remove(cell)

        # Mark the cell as safe -> MAKES NO SENSE!!
        #self.mark_safe(cell)

        # Remove the cell from safes
        if cell in self.safes:
            self.safes.remove(cell)

        # Add sentence to AI's knowledge
        neighbors = self.get_neighbors(cell)
        new_sentence = Sentence(neighbors, count)
        print("adding sentence", new_sentence)
        self.add_sentence(new_sentence)
        self.print_knowledge("\nnew knowledge", self.knowledge)

        # Mark additional cells as safe
        if count == 0:
            for neighbor in neighbors:
                if neighbor not in self.moves_made:
                    self.mark_safe(neighbor)

        # TODO Mark additional cells as mines 
        if count == len(neighbors):
            print("marking mines 1", neighbors)
            for neighbor in neighbors:
                if neighbor not in self.moves_made:
                    self.mark_mine(neighbor)

        # TODO Add new sentences
        for sentence in self.knowledge:
            if len(sentence.cells) == sentence.count:
                print("marking mines 2", sentence.cells)
                for cell in sentence.cells.copy():
                    self.mark_mine(cell)
            elif sentence.count == 0:
                for cell in sentence.cells.copy():
                    self.mark_safe(cell)
            """ elif len(sentence.safes) > 0:
                for cell in sentence.safes:
                    self.mark_safe(cell)
            elif len(sentence.mines) > 0:
                for cell in sentence.mines:
                    self.mark_mine(cell) """

        # Infer new sentences
        print("infer new sentences")
        safe_sentences = set()
        sentences_to_add = set()
        for sentence in self.knowledge:
            for other_sentence in self.knowledge:
                if sentence != other_sentence:
                    if sentence.cells.issubset(other_sentence.cells):
                        new_cells = other_sentence.cells - sentence.cells
                        new_count = other_sentence.count - sentence.count

                        if len(new_cells) == new_count:
                            print("marking mines (inferred)", new_cells, new_count)
                            for cell in new_cells:
                                self.mark_mine(cell)
                            continue

                        new_sentence = Sentence(new_cells, new_count)

                        if new_count == 0:
                            safe_sentences.add(new_sentence)
                        elif new_sentence not in self.knowledge:
                            sentences_to_add.add(new_sentence)

        if len(sentences_to_add) > 0:
            self.print_knowledge("sentences to add: ", sentences_to_add)
            for sentence in sentences_to_add:
                self.add_sentence(sentence)

        if len(safe_sentences) > 0:
            self.print_knowledge("safe sentences: ", safe_sentences)
            for sentence in safe_sentences:
                for cell in sentence.cells.copy():
                    self.mark_safe(cell)

        # Check for mines
        for sentence in self.knowledge:
            if len(sentence.cells) == sentence.count:
                print("marking mines 3", sentence.cells)
                for cell in sentence.cells.copy():
                    self.mark_mine(cell)

        # Remove empty sentences
        self.knowledge = set([sentence for sentence in self.knowledge if len(sentence.cells) > 0 and sentence.count > 0])
        print("")
        print("moves", self.moves_made)
        print("safes", self.safes)
        print("mines", self.mines)
        self.print_knowledge("knowledge", self.knowledge)
        print("\n-----")

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        if len(self.safes) == 0:
            return None
        return list(self.safes)[0]

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        cells_number = self.height * self.width
        if len(self.moves_made) + len(self.mines) == cells_number:
            return None
        
        while True:
            x = random.randrange(self.height)
            y = random.randrange(self.width)
            cell = (x, y)
            if cell not in self.moves_made and cell not in self.mines:
                return cell

    def get_neighbors(self, cell):
        """
        Returns all neighbors for a given cell
        """
        neighbors = set()
        for i in range(cell[0] - 1, cell[0] + 2):
            if i < 0 or i >= self.height:
                continue

            for j in range(cell[1] - 1, cell[1] + 2):
                if ((i, j) in self.safes or (i, j) in self.moves_made or (i, j) in self.mines or i == cell[0] and j == cell[1]) or j < 0 or j >= self.width:
                    continue

                neighbors.add((i, j))
                
        return neighbors
    
    def print_knowledge(self, title, knowledge):
        print(title + "\n", "\n".join(list(map(str, knowledge))))

    def print_board(self):
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) in self.moves_made:
                    print("|" + str(self.counts[i][j]), end="")
                else:
                    print("|-", end="")
            print("|")
