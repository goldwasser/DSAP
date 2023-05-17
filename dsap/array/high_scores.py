"""Provides GameEntry and Scoreboard class for a high-score board case study."""

class GameEntry:
    """Represents one entry of a list of high scores."""
    def __init__(self, name, score):
        """Create an entry with given name and score."""
        self._name = name
        self._score = score

    def get_name(self):
        """Return the name of the person for this entry."""
        return self._name

    def get_score(self):
        """Return the score of this entry."""
        return self._score

    def __str__(self):
        """Return string representation of the entry."""
        return f'({self._name}, {self._score})' # e.g., '(Bob, 98)'

class Scoreboard:
    """Fixed-length sequence of high scores in nondecreasing order."""
    def __init__(self, capacity=10):
        """Initialize scoreboard with given maximum capacity.

        All entries are initially None.
        """
        self._board = [None] * capacity             # reserve space for future scores
        self._n = 0                                 # number of actual entries

    def __getitem__(self, k):
        """Return entry at index k."""
        return self._board[k]

    def __str__(self):
        """Return string representation of the high score list."""
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        """Consider adding entry to high scores."""
        new_score = entry.get_score()

        # Does new entry qualify as a high score?
        # answer is yes if board not full or new score is higher than last entry
        good = self._n < len(self._board) or new_score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):          # no score drops from list
                self._n += 1                        # so overall number increases

            # shift lower scores rightward to make room for new entry
            j = self._n - 1
            while j > 0 and self._board[j-1].get_score() < new_score:
                self._board[j] = self._board[j-1]   # shift entry from j-1 to j
                j -= 1                              # and decrement j
            self._board[j] = entry                  # when done, add new entry

if __name__ == '__main__':
    board = Scoreboard(5)
    for e in (('Rob', 750), ('Mike',1105), ('Rose', 590), ('Jill', 740),
              ('Jack', 510), ('Anna', 660), ('Paul', 720), ('Bob', 400),
              ):
        ge = GameEntry(e[0], e[1])
        board.add(ge)
        print(f'After considering {ge}, scoreboard is:')
        print(board)
        print()
