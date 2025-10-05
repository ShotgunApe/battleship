from enum import Enum

class GameState(Enum):
    PLAYER = 0
    CPU = 1

class Game:
    def __init__(self):
        self.curState = GameState.PLAYER

    def setState(self, state):
        self.curState = state

    def getState(self):
        return self.curState