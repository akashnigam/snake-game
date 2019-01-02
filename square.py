import pygame


class Square:

    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

    def draw(self, screen, color, addEye=0, eyeColor=(255, 255, 255)):
        # to keep square inside grid -2 and +1 in following
        side_length = self.side_length - 2
        start_x = self.x * self.side_length + 1
        start_y = self.y * self.side_length + 1
        rect = (start_x, start_y, side_length, side_length)
        pygame.draw.rect(screen, color, rect)
        if addEye == 1:
            circle_x = int((start_x + start_x + side_length)/2)
            circle_y = int((start_y + start_y + side_length)/2)
            circle_pos = (circle_x, circle_y)
            radius = 1
            pygame.draw.circle(screen, eyeColor, circle_pos, radius)
