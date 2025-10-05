class Ship:
    def __init__(self, size):
        self.size = size
        self.coords = []

    def getCoords(self):
        return self.coords

    def setCoords(self, coord):
        self.coords.append(coord)

    def display(self):
        return f"{self.size, self.coords}"