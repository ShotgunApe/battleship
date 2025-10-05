# god i hate python imports
import utils.ships as Ship
import utils.board as Board
import utils.game as Game

def main():
    # Create Board object - Board(size)
    board = Board.Board(10)

    # Create Ship objects
    ships = []
    for i in range(1, 6):
        ships.append(Ship.Ship(i))
    
    # Generate ship coords
    board.randomizeShips(ships)
    
    # Configure board state
    for ship in ships:
        board.setState(ship.getCoords())

    board.display()

    # Create game state + begin loop

if __name__ == "__main__":
    main()