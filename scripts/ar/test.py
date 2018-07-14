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
#width,height = 2048,1152

def setup():
    """ Setup window and pygame environment """
    pygame.init()
    pygame.display.set_mode((width, height), OPENGL|DOUBLEBUF)
    pygame.display.set_caption('OpenGL AR demo')

def rotate(degrees, K, Rt, width, height, img):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    ar.draw_background(img)
    ar.set_projection_from_camera(K, width, height)
    ar.set_modelview_from_camera(Rt)
    ar.draw_teapot(0.1, degrees)
    draw_teapots()
    pygame.display.flip()

def draw_teapots():
    for i in [0.2, 0, -0.2]:
        for j in [0.2, 0, -0.2]:
            glPushMatrix()
            if not (i==0 and j==0):
                ar.draw_teapot(0.05, pos=[i,0,j])
            glPopMatrix()

if __name__=="__main__":
    # load camera data
    #with open("../../data/ar_camera.pkl", "r") as f:
    with open("../../data/ar_camera_mag.pkl", "rb") as f:
        K = pickle.load(f)
        Rt = pickle.load(f)

    setup()
    #img = '../../data/book_perspective.jpg'
    img = '../../data/mag_perspective.jpg'
    ar.draw_background(img)
    ar.set_projection_from_camera(K, width, height)
    ar.set_modelview_from_camera(Rt)
    ar.draw_teapot(0.1)
    #draw_teapots()
    pygame.display.flip()

    clock = pygame.time.Clock()
    degrees = [0,0,0]
    ticker = 10
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
        #degrees[0] += 10
        #degrees[0] %= 360
        """ Simply flipping creates flicker
        but redrawing followed by flipping removes the flicker """ 
        rotate(degrees, K, Rt, width, height, img) # includes flip()
        #pygame.display.flip()
        clock.tick(ticker)
        #time.sleep(0.1)
