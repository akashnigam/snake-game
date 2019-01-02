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
        self.squares_pos = []

    def change_direction(self, event):
        # to prevent snake from turning in axis along which it is already moving
        if self.head_dir["x_dir"] in [-1,1] and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            return
        elif self.head_dir["y_dir"] in [-1,1] and event.key in [pygame.K_UP, pygame.K_DOWN]:
            return

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
        self.squares_pos = self.get_squares_pos()
        return self.assert_not_intersecting()

    def get_squares_pos(self):
        squares_pos_list = []
        square_x = self.head_pos["x"]
        square_y = self.head_pos["y"]
        turn_index = 0
        turn_list = self.turn_list
        dirc = self.head_dir
        for i in range(0, self.length):
            new_square_pos = (square_x, square_y)
            squares_pos_list.append(new_square_pos)
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
        return squares_pos_list


    def assert_not_intersecting(self):
        pos_dict = {}
        for square_pos in self.squares_pos:
            if square_pos in pos_dict:
                return False
            pos_dict[square_pos] = 1
        return True

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
                sq.draw(screen, self.head_color, 1)
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
