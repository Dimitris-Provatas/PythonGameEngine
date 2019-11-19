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
    
    # Class Variables
    x_move = 0
    y_move = 0
    z_move = 0

    def __init__(self):
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

        gluPerspective(90, (display[0]/display[1]), 0.1, 50.0) # (FOV, Resolution, NearClippingPlane, FarClippingPlane)
        
        glTranslatef(0.0, 0.0, -5) # (x, y, z)

        #glRotatef(25, 5, 5, 5)

        # Cube Spawn
        for i in range(10):
            Cube.__init__(Cube, i, i, i)

        while True:
            self.main(self)

    def main(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Keydown inputs
            if event.type == KEYDOWN:
                #Quit
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()

                # X axis is left and right
                # Y axis is up and down
                # Z axis is forwards and backwards

                #Left
                if event.key == pygame.K_a:
                    self.x_move = 0.1
                #Right
                if event.key == pygame.K_d:
                    self.x_move = -0.1
                #Forward
                if event.key == pygame.K_w:
                    self.z_move = 0.1
                #Backward
                if event.key == pygame.K_s:
                    self.z_move = -0.1

            # Keyup inputs
            if event.type == KEYUP:

                # x axis is left and right
                # y axis is up and down
                # z axis is forwards and backwards

                # Stops movement on X axis
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    self.x_move = 0

                # Stops movement on Z axis
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    self.z_move = 0

                # Rotation will be on mouse move

                # #Rotate Left
                # if event.key == pygame.K_q:
                #     glRotatef(5, 0, 1, 0)
                # #Rotate Right
                # if event.key == pygame.K_e:
                #     glRotatef(-5, 0, 1, 0)

                # #Rotate Left
                # if event.key == pygame.K_q:
                #     glRotatef(5, 0, 1, 0)
                # #Rotate Right
                # if event.key == pygame.K_e:
                #     glRotatef(-5, 0, 1, 0)

            # Unneeded for the time

            # # Mouse inputs
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     #Mouse wheel

            #     #Upwards
            #     if event.button == 4:
            #         glTranslatef(0, 0, -0.5)
            #     #Downwards
            #     if event.button == 5:
            #         glTranslatef(0, 0, 0.5

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Camera Works
        camera = glGetDoublev(GL_MODELVIEW_MATRIX)
        
        camera_x = camera[3][0]
        camera_y = camera[3][1]
        camera_z = camera[3][2]
        #print("x= ", camera_x, ", y=", camera_y, ", z= ", camera_x)

        glTranslatef(self.x_move, self.y_move, self.z_move)

        pygame.display.flip()
        pygame.time.wait(1) # in milisecs
