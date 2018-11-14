import square
import pygame
import copy


class Snake:

    def __init__(self, square_side, width, height, color, head_color):
        self.board_height = height
        self.board_width = width
        self.square_side = square_side
        self.color = color
        self.head_color = head_color
        self.head_dir = {"x_dir": 1, "y_dir": 0}
        self.head_pos = {"x": 0, "y": (height/square_side)/2}
        self.length = 1
        self.turn_list = []

    def change_direction(self, event):
        head_pos = copy.copy(self.head_pos)
        head_dir = copy.copy(self.head_dir)
        self.turn_list.insert(0, {"pos": head_pos, "dir": head_dir})
        if event.key == pygame.K_LEFT:
            self.head_dir["x_dir"] = -1
            self.head_dir["y_dir"] = 0
        elif event.key == pygame.K_RIGHT:
            self.head_dir["x_dir"] = 1
            self.head_dir["y_dir"] = 0
        elif event.key == pygame.K_UP:
            self.head_dir["x_dir"] = 0
            self.head_dir["y_dir"] = -1
        elif event.key == pygame.K_DOWN:
            self.head_dir["x_dir"] = 0
            self.head_dir["y_dir"] = 1

    def move(self):
        self.head_pos["x"] += self.head_dir["x_dir"]
        self.head_pos["x"] %= (self.board_width//self.square_side)
        self.head_pos["y"] += self.head_dir["y_dir"]
        self.head_pos["y"] %= (self.board_height // self.square_side)

    def eat_food_if_exist(self, food_obj):
        if food_obj.x == self.head_pos["x"] and food_obj.y == self.head_pos["y"]:
            self.length += 1
            return True
        return False

    def draw(self, screen):
        turn_list = self.turn_list
        dirc = self.head_dir
        turn_index = 0
        square_x = self.head_pos["x"]
        square_y = self.head_pos["y"]
        for i in range(0, self.length):
            sq = square.Square(square_x, square_y, self.square_side)
            if self.head_pos["x"] == square_x and self.head_pos["y"] == square_y:
                sq.draw(screen, self.head_color)
            else:
                sq.draw(screen, self.color)
            prev_sq_x = square_x
            prev_sq_y = square_y
            square_x = prev_sq_x - (dirc["x_dir"])
            square_y = prev_sq_y - (dirc["y_dir"])
            new_square_pos = (square_x, square_y)
            if turn_index < len(turn_list):
                turn_pos = turn_list[turn_index]["pos"]
                turn_pos_tuple = (turn_pos["x"], turn_pos["y"])
                if new_square_pos == turn_pos_tuple:
                    dirc = turn_list[turn_index]["dir"]
                    turn_index += 1
                    if i == self.length - 1:
                        turn_list.pop()
