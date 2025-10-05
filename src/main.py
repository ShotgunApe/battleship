# god i hate python imports
import utils.ships as Ship
import utils.board as Board
import utils.game as Game

import random

def main():
    # Create Board object - Board(size)
    board = Board.Board(10)

    # Create Ship objects
    ships = []
    for i in range(1, 6):
        ships.append(Ship.Ship(i))
    
    # Generate ship coords
    for ship in ships:
        ship.setCoords((random.randint(0, 9), random.randint(0, 9)))
        print(ship.display())

if __name__ == "__main__":
    main()