import pygame as game
import sys


class Game:
    def __init__(self):
        game.init()
        self.screen = game.display.set_mode((800, 600))
        game.display.set_caption("My Game")
        self.clock = game.time.Clock()
        self.running = True




if __name__ == "__main__":
    game = Game()
