# Catan! Started March 23, 2011

import os
import random
import sys

import Tkinter
from Tkinter import *

import pygame
from pygame.locals import *

sys.path.append("game") 
import board
from board import Board
from board import Resources


def input(events): 
    for event in events: 
        if event.type == QUIT: 
            pygame.quit()
            sys.exit(0) 

            
def init_gui(board, Tiles, Rolls):
    # pygame setup:
    pygame.init()
    window = pygame.display.set_mode((900, 600)) 
    pygame.display.set_caption('Catan') 
    window.fill((15,180,255)) # set background to blue
    screen = pygame.display.get_surface() 
    
    image_src_path = "C:\\Users\\gnleece\\Coding\\Catan\\images\\"
    tile_imgs = {}
    tile_imgs[Resources.Clay] = pygame.image.load(image_src_path + "clay.png")
    tile_imgs[Resources.Wood] = pygame.image.load(image_src_path + "wood.png")
    tile_imgs[Resources.Sheep] = pygame.image.load(image_src_path + "sheep.png")
    tile_imgs[Resources.Wheat] = pygame.image.load(image_src_path + "wheat.png")
    tile_imgs[Resources.Ore] = pygame.image.load(image_src_path + "ore.png")
    tile_imgs[Resources.Desert] = pygame.image.load(image_src_path + "desert.png")
    
    roll_imgs = {}
    for i in range(2,13):
        if i != 7:
            roll_imgs[i] = pygame.image.load(image_src_path + str(i) + ".png")
    
    # set transparency colour:  
    for tile in tile_imgs:
        tile_imgs[tile].set_colorkey((255,0,255))    
    for roll in roll_imgs:
        roll_imgs[roll].set_colorkey((255,0,255))
    
    vert_offset = 65
    horiz_offset = 250
    height = 89
    width = 80
    
    board.hexagons[0].set_pos(horiz_offset, 1*height+vert_offset) 
    board.hexagons[1].set_pos(horiz_offset, 2*height+vert_offset)
    board.hexagons[2].set_pos(horiz_offset, 3*height+vert_offset)
    
    board.hexagons[3].set_pos(horiz_offset+width, 0.5*height+vert_offset)
    board.hexagons[4].set_pos(horiz_offset+width, 1.5*height+vert_offset)
    board.hexagons[5].set_pos(horiz_offset+width, 2.5*height+vert_offset)
    board.hexagons[6].set_pos(horiz_offset+width, 3.5*height+vert_offset)
    
    board.hexagons[7].set_pos(horiz_offset+2*width, 0*height+vert_offset) 
    board.hexagons[8].set_pos(horiz_offset+2*width, 1*height+vert_offset)    
    board.hexagons[9].set_pos(horiz_offset+2*width, 2*height+vert_offset)
    board.hexagons[10].set_pos(horiz_offset+2*width, 3*height+vert_offset)
    board.hexagons[11].set_pos(horiz_offset+2*width, 4*height+vert_offset)
    
    board.hexagons[12].set_pos(horiz_offset+3*width, 0.5*height+vert_offset)
    board.hexagons[13].set_pos(horiz_offset+3*width, 1.5*height+vert_offset)
    board.hexagons[14].set_pos(horiz_offset+3*width, 2.5*height+vert_offset)
    board.hexagons[15].set_pos(horiz_offset+3*width, 3.5*height+vert_offset)
    
    board.hexagons[16].set_pos(horiz_offset+4*width, 1*height+vert_offset) 
    board.hexagons[17].set_pos(horiz_offset+4*width, 2*height+vert_offset)
    board.hexagons[18].set_pos(horiz_offset+4*width, 3*height+vert_offset)

    board.finalize()
    
    offset = 0
    for i in range(0,19):
        if Tiles[i] == Resources.Desert:
            offset = 1
            board.hexagons[i].set_tile(Tiles[i], tile_imgs[Tiles[i]], -1)
        else:
            board.hexagons[i].set_tile(Tiles[i], tile_imgs[Tiles[i]], 
                                       Rolls[i-offset], roll_imgs[Rolls[i-offset]])

    for hexagon in board.hexagons:
        hexagon.draw(screen)
        print str(hexagon.resource) + " " + str(hexagon.roll)
    
    #myfont = pygame.font.SysFont("Comic Sans MS", 30) 
    #label = myfont.render("test!", 1, (0,0,0))
    #screen.blit(label, (100, 100))
        
    red_dot = pygame.image.load(image_src_path + "red_dot.png")
    red_dot.set_colorkey((255,0,255))   
    
    green_dot = pygame.image.load(image_src_path + "green_dot.png")
    green_dot.set_colorkey((255,0,255))   
    
    yellow_dot = pygame.image.load(image_src_path + "yellow_dot.png")
    yellow_dot.set_colorkey((255,0,255))  
    
    #board.draw_vertices(screen, red_dot)
    
    #board.vertices[2].draw_neighbourhood(screen, green_dot, yellow_dot, board)
    
    pygame.display.flip() 
    

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        
        canvas = Canvas(master)

        import Image, ImageTK
        self.image = Image.open("C:\\Users\\gnleece\\Coding\\Catan\\images\\sheep.gif")
        self.photo = ImageTk.PhotoImage(self.image)
        item = canvas.create_image(0, 0, image=photo)

        canvas.pack()

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hi there, everyone!"    
    
def main():
    board = Board(3)
    Tiles = Resources.Tiles
    random.shuffle(Tiles)  
    Rolls = Resources.Rolls
    random.shuffle(Rolls)

    #init_gui(board, Tiles, Rolls)
    
    # main game loop:
    #while True: 
    #    input(pygame.event.get()) 

    root = Tk()
    app = App(root)
    
    root.mainloop()
        
if __name__ == "__main__":
    main()