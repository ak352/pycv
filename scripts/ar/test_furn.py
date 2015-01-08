from OpenGL.GL import *
from OpenGL.GLU import *
import pygame, pygame.image
from pygame.locals import *
import ar
import pickle
import time
from scipy import *
from numpy import *
import sys
sys.path.append("../objloader")
import objloader
import cPickle

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
    #img = '../../data/book_perspective.jpg'
    img = "../../data/mag_front.jpg"
    #img  = "../../data/mag_perspective.jpg"
    #img = "../../data/mag_perspective_1.jpg"
    pkl = img[:-4]+".pkl"
    #with open("../../data/ar_camera.pkl", "r") as f:
    with open(pkl, "r") as f:
        K = pickle.load(f)
        Rt = pickle.load(f)

    setup()
    glEnable(GL_NORMALIZE)
    ar.draw_background(img)
    ar.set_projection_from_camera(K, width, height)
    ar.set_modelview_from_camera(Rt)

    """ Load once into memory as this is time-taking """
    #obj = objloader.OBJ("toyplane.obj")
    obj = objloader.OBJ("Sofa_3_3ds.obj")
    #obj_2 = objloader.OBJ("toyplane.obj")
#     obj = None
#     with open("../objloader/toyplane.pkl", 'rb') as input:
#         obj = cPickle.load(input)
#     if not obj:
#         sys.exit()

    #(scale, degrees, pos) = (0.001486436280241436, [0, -5, 0], [0.09500000000000001, 0, 0.10500000000000002])
    degrees = [0,0,0]
    pos = [0,0,0]
    scale = 0.005

    ar.draw_furniture(obj, scale)
    pygame.display.flip()

    clock = pygame.time.Clock()
    ticker = 30
    rotate_unit = 0
    translate_unit = [0,0,0]
    scale_unit = 1
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                break
            if event.type == KEYDOWN: 
                if event.key == K_UP:
                    #degrees[0] += 10
                    translate_unit[0] = 0.005
                if event.key == K_DOWN:
                    #degrees[0] -= 10
                    translate_unit[0] = -0.005
                if event.key == K_RIGHT:
                    #degrees[1] += 10
                    translate_unit[2] = -0.005
                if event.key == K_LEFT:
                    #degrees[1] -= 10
                    translate_unit[2] = 0.005
                if event.key == K_MINUS:
                    scale_unit = 1/1.1
                    #print scale_unit
                if event.key == K_PERIOD:
                    scale_unit = 1.1
                    #print scale_unit
                if event.key == K_q:
                    rotate_unit = 5
                if event.key == K_s:
                    rotate_unit  = -5
            if event.type == KEYUP:
                if event.key == K_q or event.key == K_s:
                    rotate_unit = 0
                if event.key in (K_UP, K_DOWN):
                    translate_unit[0] = 0
                    #print translate_unit
                if event.key in (K_LEFT, K_RIGHT):
                    translate_unit[2] = 0
                    #print translate_unit
                if event.key in (K_PERIOD, K_MINUS):
                    scale_unit = 1

        for i,x in enumerate(pos):
            pos[i] += translate_unit[i]
        degrees[1] += rotate_unit
        scale *= scale_unit
        print (scale, degrees, pos)
        #degrees[0] += 10
        #degrees[0] %= 360
        """ Simply flipping creates flicker
        but redrawing followed by flipping removes the flicker """ 
        #rotate(degrees, K, Rt, width, height, img) # includes flip()
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        ar.draw_background(img)
        ar.set_projection_from_camera(K, width, height)
        ar.set_modelview_from_camera(Rt)
        ar.draw_teapot(scale, degrees, pos)
        #ar.draw_furniture(obj, scale, degrees, pos)
        #ar.draw_furniture(obj_2, scale, degrees, pos)
        pygame.display.flip()
        clock.tick(ticker)
        #time.sleep(0.1)
