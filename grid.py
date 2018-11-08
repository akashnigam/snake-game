import pygame


class Grid:
    def __init__(self, square_side, width, height):
        self.square_side = square_side
        self.width = width
        self.height = height

    def draw(self, screen, color):
        nv = self.width // self.square_side + 1
        nh = self.height // self.square_side + 1
        for i in range(0, nv):
            start_coordinate = (i * self.square_side, 0)
            end_coordinate = (i * self.square_side, self.height)
            pygame.draw.line(screen, color, start_coordinate, end_coordinate)
        for j in range(0, nh):
            start_coordinate = (0, j * self.square_side)
            end_coordinate = (self.width, j * self.square_side)
            pygame.draw.line(screen, color, start_coordinate, end_coordinate)
