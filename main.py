import pygame
import random

#Shapes of the blocks
shapes = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[2, 1, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]
#Colors of the blocks
shapeColors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

# GLOBALS VARS
width = 700
height = 600
gameWidth = 100  # meaning 300 // 10 = 30 width per block
gameHeight = 400  # meaning 600 // 20 = 20 height per blo ck
blockSize = 20
 
topLeft_x = (width - gameWidth) // 2
topLeft_y = height - gameHeight - 50

class Block:
    x = 0
    y = 0
    n = 0
    def __init__(self, x, y,n):
        self.x = x
        self.y = y
        self.type = n
        self.color = n
        self.rotation = 0
    def image(self):
        return shapes[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(shapes[self.type])

class Tetris:
    level = 2
    score = 0
    state = "start"
    field = []
    height = 0
    width = 0
    zoom = 20
    x = 100
    y = 60
    block = None
    nextBlock=None

