import pygame
import grid
import food
import sys


class Game:

    def __init__(self, width, height, square_side, grid_color, snake_color, food_color, bg_color):
        self.width = width
        self.height = height
        self.grid_color = grid_color
        self.snake_color = snake_color
        self.food_color = food_color
        self.square_side = square_side
        self.bg_color = bg_color

    def draw(self):
        screen_size = (self.width, self.height)
        screen = pygame.display.set_mode(screen_size)
        grid_instance = grid.Grid(self.square_side, self.width, self.height, self.grid_color)
        food_generator = food.Food(self.square_side, self.width, self.height, self.food_color)
        food_generator.create_food()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            screen.fill(self.bg_color)
            grid_instance.draw(screen)
            food_generator.draw(screen)
            pygame.display.flip()

    def start(self):
        self.draw()


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

board_width = 100
board_height = 100
board_square_side = 10
board_grid_color = white
board_snake_color = green
board_food_color = blue
board_bg_color = black
game = Game(board_width, board_height, board_square_side, board_grid_color, board_snake_color, board_food_color,
            board_bg_color)
game.start()
