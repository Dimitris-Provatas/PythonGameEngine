# General Python Imports
import random

# Game Engine Imports

# PyGames
import pygame
from pygame.locals import *

# OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

class Cube(object):

    x = y = z = 0

    verticies = (
        # center is 0, 0, 0
        # x,  y,  z
        ( 1, -1, -1), #0
        ( 1,  1, -1), #1
        (-1,  1, -1), #2
        (-1, -1, -1), #3
        ( 1, -1,  1), #4
        ( 1,  1,  1), #5
        (-1, -1,  1), #6
        (-1,  1,  1)  #7
    )

    edges = (
        (0, 1), #0
        (0, 3), #1
        (0, 4), #2
        (2, 1), #3
        (2, 3), #4
        (2, 7), #5
        (6, 3), #6
        (6, 4), #7
        (6, 7), #8
        (5, 1), #9
        (5, 4), #10
        (5, 7)  #11
    )

    surfaces = (
        (0, 1, 2, 3), #0
        (3, 2, 7, 6), #1
        (6, 7, 5, 4), #2
        (4, 5, 1, 0), #3
        (1, 5, 7, 2), #4
        (4, 0, 3, 6)  #5
    )

    colours = (
        #r, g, b
        (1, 0, 0), #0 red
        (0, 1, 0), #1 green
        (0, 0, 1), #2 blue
        (0, 0, 0), #3 black
        (1, 1, 1)  #4 white
    )

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.render(self)

    # Render Cube
    def render(self):
        glBegin(GL_QUADS)

        for surface in self.verticies:
            for vertex in surface:
                glColor3fv(self.colours[2])
                glVertex3fv(self.verticies[vertex])

        glEnd()

        glBegin(GL_LINES)

        for edge in self.edges:
            for vertex in edge:
                glColor3fv(self.colours[4])
                glVertex3fv(self.verticies[vertex])

        glEnd()