from OpenGL.GL import *
from OpenGL.GLU import *
import pygame, pygame.image
from pygame.locals import *
import ar

width,height=1000,747

def setup():
    """ Setup window and pygame environment """
    pygame.init()
    pygame.display.set_mode((width, height), OPENGL|DOUBLEBUF)
    pygame.display.set_caption('OpenGL AR demo')

if __name__=="__main__":
    setup()
    ar.draw_background('../../data/labr.jpg')
    ar.draw_teapot(0.1)


    while True:
        event = pygame.event.poll()
        if event.type in (QUIT, KEYDOWN):
            break
        pygame.display.flip()

