import pygame


class Square:
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

    def draw(self, screen, color):
        # to keep square inside grid -2 and +1 in following
        side_length = self.side_length - 2
        start_x = self.x * self.side_length + 1
        start_y = self.y * self.side_length + 1
        rect = (start_x, start_y, side_length, side_length)
        pygame.draw.rect(screen, color, rect)
