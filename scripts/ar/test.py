from OpenGL.GL import *
from OpenGL.GLU import *
import pygame, pygame.image
from pygame.locals import *
import ar
import pickle
import time
from scipy import *
from numpy import *

width,height=1000,747

def setup():
    """ Setup window and pygame environment """
    pygame.init()
    pygame.display.set_mode((width, height), OPENGL|DOUBLEBUF|HWSURFACE)
    pygame.display.set_caption('OpenGL AR demo')

def rotate(event_type, degrees, K, Rt, width, height, img):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    ar.draw_background(img)
    ar.set_projection_from_camera(K, width, height)
    ar.set_modelview_from_camera(Rt)
    ar.draw_teapot(0.1, degrees)
    pygame.display.flip()


if __name__=="__main__":
    # load camera data
    with open("../../data/ar_camera.pkl", "r") as f:
        K = pickle.load(f)
        Rt = pickle.load(f)

    setup()
    img = '../../data/book_perspective.jpg'
    ar.draw_background(img)
    ar.set_projection_from_camera(K, width, height)
    ar.set_modelview_from_camera(Rt)
    ar.draw_teapot(0.1)

    
    pygame.display.flip()

    degrees = [0,0,0]
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                break
            if event.type == KEYDOWN: 
                if event.key == K_UP:
                    degrees[0] += 10
                if event.key == K_DOWN:
                    degrees[0] -= 10
                if event.key == K_RIGHT:
                    degrees[1] += 10
                if event.key == K_LEFT:
                    degrees[1] -= 10
                if event.key in (K_UP, K_DOWN, K_RIGHT, K_LEFT):
                    rotate(event.key, degrees, K, Rt, width, height, img)
        #pygame.display.flip()
        #time.sleep(0.1)
