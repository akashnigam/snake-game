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
            eye_start_x = int((start_x + start_x + side_length)/2)-1
            eye_start_y = int((start_y + start_y + side_length)/2)-1
            eye_rect = (eye_start_x, eye_start_y, 2, 1)
            pygame.draw.rect(screen, eyeColor, eye_rect)
