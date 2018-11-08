import square
import pygame


class Snake:

    def __init__(self, square_side, width, height, color):
        self.board_height = height
        self.board_width = width
        self.square_side = square_side
        self.color = color
        self.x_dir = 1
        self.y_dir = 0
        self.head_x = 0
        self.head_y = (height/square_side)/2
        self.length = 1

    def change_direction(self, event):
        if event.key == pygame.K_LEFT:
            self.x_dir = -1
            self.y_dir = 0
        elif event.key == pygame.K_RIGHT:
            self.x_dir = 1
            self.y_dir = 0
        elif event.key == pygame.K_UP:
            self.x_dir = 0
            self.y_dir = -1
        elif event.key == pygame.K_DOWN:
            self.x_dir = 0
            self.y_dir = 1

    def move(self):
        self.head_x += self.x_dir
        self.head_x %= (self.board_width//self.square_side)
        self.head_y += self.y_dir
        self.head_y %= (self.board_height // self.square_side)

    def eat_food_if_exist(self, food_obj):
        if food_obj.x == self.head_x and food_obj.y == self.head_y:
            self.length += 1
            return True
        return False

    def draw(self, screen):
        for i in range(0, self.length):
            square_x = self.head_x - (i * self.x_dir)
            square_y = self.head_y - (i * self.y_dir)
            sq = square.Square(square_x, square_y, self.square_side)
            if self.head_x == square_x and self.head_y == square_y:
                sq.draw(screen, (0, 0, 255))
            else:
                sq.draw(screen, self.color)
