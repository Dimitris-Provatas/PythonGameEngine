#################
#   IMPORTS     #
#################

# Game Engine Imports
from classes.cube import Cube

# PyGames
import pygame
from pygame.locals import *

# OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *


class engine():

    def __init__(self):
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

        gluPerspective(90, (display[0]/display[1]), 0.1, 50.0) # (FOV, Resolution, NearClippingPlane, FarClippingPlane)
        
        glTranslatef(0.0, 0.0, -5) # (x, y, z)

        #glRotatef(25, 5, 5, 5)

        # Cube Spawn

        while True:
            self.main(self)

    def main(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Key inputs
            elif event.type == KEYDOWN:
                #Quit
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()

                #Left
                if event.key == pygame.K_a:
                    glTranslatef(0.1, 0, 0)
                #Right
                if event.key == pygame.K_d:
                    glTranslatef(-0.1, 0, 0)
                #Up
                if event.key == pygame.K_w:
                    glTranslatef(0, -0.1, 0)
                #Down
                if event.key == pygame.K_s:
                    glTranslatef(0, 0.1, 0)

                #Rotate Left
                if event.key == pygame.K_q:
                    glRotatef(5, 0, 1, 0)
                #Rotate Right
                if event.key == pygame.K_e:
                    glRotatef(-5, 0, 1, 0)

            # Mouse inputs
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #Mouse wheel

                #Upwards
                if event.button == 4:
                    glTranslatef(0, 0, -0.5)
                #Downwards
                if event.button == 5:
                    glTranslatef(0, 0, 0.5)
                    
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for x in range(10):
            Cube.__init__(Cube, 5, 3, 7)

        # Camera Works
        camera = glGetDoublev(GL_MODELVIEW_MATRIX)
        
        camera_x = camera[3][0]
        camera_y = camera[3][1]
        camera_z = camera[3][2]
        #print("x= ", camera_x, ", y=", camera_y, ", z= ", camera_x)

        pygame.display.flip()
        pygame.time.wait(1) # in milisecs
