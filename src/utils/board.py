import random

class Board:
    def __init__(self, size):
        self.boardState = [[False for _ in range(size)] for _ in range(size)]

    def setState(self, coords):
        for coord in coords:
            x = coord[0]
            y = coord[1]
            self.boardState[x][y] = True

    def commonCoords(self, listOne, listTwo):
        for sublist in listOne:
            if sublist in listTwo:
                return True
            else:
                return False

    def randomizeShips(self, ships):
        takenCoords = []
        for ship in ships:
            conflict = True

            # Generate random (x, y) and orientation - ensuring it is not used already
            while (conflict):
                gen = [random.randint(0, 9), random.randint(0, 9)]
                xory = random.choice([0, 1])

                # Helper vars
                tmpCoords = []
                mvFlag = False

                # Correct to avoid OOB
                if (ship.getSize() > 9 - gen[xory]):
                    gen[xory] = gen[xory] - ship.getSize()
                    mvFlag = True

                # Place extension in tmp list now that we know there is no overflow
                for i in range(0, (ship.getSize())):
                    gen[xory] += 1
                    tmpCoords.append(gen[:]) # Shallow copy

                # Actually check for overlapping errors now
                if not self.commonCoords(tmpCoords, takenCoords):
                    for i in range(0, (ship.getSize())):
                        gen[xory] -= 1
                        ship.setCoords(gen[:])
                        takenCoords.append(gen[:])

                    conflict = False

    def display(self):
        for x in range(0, len(self.boardState)):
            for y in range(0, len(self.boardState[0])):
                if (self.boardState[x][y]):
                    print(f"[o]", end="")
                else:
                    print(f"[ ]", end="")
            print("")
