import random
import square


class Food:

    def __init__(self, square_side, height, width, color):
        self.height = height
        self.width = width
        self.square_side = square_side
        self.color = color
        self.x = 0
        self.y = 0

    def create_food(self):
        nv = self.width // self.square_side
        nh = self.height // self.square_side
        self.x = random.randint(0, nv-1)
        self.y = random.randint(0, nh-1)

    def draw(self, screen):
        sq = square.Square(self.x, self.y, self.square_side)
        sq.draw(screen, self.color)
