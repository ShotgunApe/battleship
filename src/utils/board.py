class Board:
    def __init__(self, size):
        self.boardState = [[False for _ in range(size)] for _ in range(size)]

    def display(self):
        return f"{self.boardState}"