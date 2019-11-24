#################
#   IMPORTS     #
#################

# Game Engine Imports
from classes.cube import Cube
from classes.renderer import Renderer

# PyGames
import pygame
from pygame.locals import *

# OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

class Engine(object):

    # Class Variables

    def __init__(self):

        # Cube Spawn
        for i in range(3):
            my_cube = Cube(i, i, i)
            Renderer.renderCube(my_cube.new_verts, my_cube.surfaces, my_cube.edges)

        while True:
            Renderer()
            self.main()

    #cubes array
    def cubeArray(self):
        return self.cubes

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
                    Renderer.x_move = 0.1
                #Right
                if event.key == pygame.K_d:
                    Renderer.x_move = -0.1
                #Forward
                if event.key == pygame.K_w:
                    Renderer.z_move = 0.1
                #Backward
                if event.key == pygame.K_s:
                    Renderer.z_move = -0.1

            # Keyup inputs
            if event.type == KEYUP:

                # x axis is left and right
                # y axis is up and down
                # z axis is forwards and backwards

                # Stops movement on X axis
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    Renderer.x_move = 0

                # Stops movement on Z axis
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    Renderer.z_move = 0

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
