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

#Sets the properties of the board
    def __init__(self, height, width):
        self.height = height
        self.width = width
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

#Creates a new block
    def new_block(self):
        self.block = Block(3, 0,random.randint(0, len(shapes) - 1))
                           
    def next_block(self):
        self.nextBlock=Block(3,0,random.randint(0, len(shapes) - 1))
    #Checks if the blocks touch the top of the board
    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.image():
                    if i + self.block.y > self.height - 1 or \
                            j + self.block.x > self.width - 1 or \
                            j + self.block.x < 0 or \
                            self.field[i + self.block.y][j + self.block.x] > 0:
                        intersection = True
        return intersection

#Checks if a row is formed and destroys that line
    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2

    def draw_next_block(self,screen):
    
        font = pygame.font.SysFont("Calibri", 30)
        label = font.render("Next Shape", 1, (128,128,128))

        sx = topLeft_x + gameWidth + 50
        sy = topLeft_y + gameHeight/2 - 100
        format = self.nextBlock.image()
        for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in self.nextBlock.image():
                        pygame.draw.rect(screen, shapeColors[self.nextBlock.color],(sx + j*30, sy + i*30, 30, 30), 0)



