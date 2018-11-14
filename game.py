import pygame
import grid
import food
import snake
import sys
from time import sleep


class Game:

    def __init__(self, width, height, square_side, grid_color, snake_color, snake_head_color, food_color, bg_color):
        self.width = width
        self.height = height
        self.grid_color = grid_color
        self.snake_color = snake_color
        self.snake_head_color = snake_head_color
        self.food_color = food_color
        self.square_side = square_side
        self.bg_color = bg_color

    def draw(self):
        screen_size = (self.width, self.height)
        screen = pygame.display.set_mode(screen_size)
        grid_instance = grid.Grid(self.square_side, self.width, self.height, self.grid_color)
        food_generator = food.Food(self.square_side, self.width, self.height, self.food_color)
        snake_instance = snake.Snake(self.square_side, self.width, self.height, self.snake_color, self.snake_head_color)
        food_generator.create_food()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    snake_instance.change_direction(event)
            screen.fill(self.bg_color)
            snake_instance.move()
            if snake_instance.eat_food_if_exist(food_generator):
                food_generator.create_food()
            grid_instance.draw(screen)
            food_generator.draw(screen)
            snake_instance.draw(screen)
            pygame.display.flip()
            sleep(0.05)


    def start(self):
        self.draw()


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
dark_green = (0, 150, 0)
blue = (0, 0, 255)

board_width = 500
board_height = 500
board_square_side = 10
board_grid_color = black
board_snake_color = green
board_snake_head_color = dark_green
board_food_color = red
board_bg_color = black
game = Game(board_width, board_height, board_square_side, board_grid_color, board_snake_color, board_snake_head_color,
            board_food_color, board_bg_color)
game.start()
