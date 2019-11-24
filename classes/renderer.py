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



class Renderer(object):

    # Class Variables

    x_move = y_move = z_move = 0
    camera_x = camera_y = camera_z = 0
    camera_tilt_x = camera_tilt_y = camera_tilt_z = 0

    camera_coords = (camera_x, camera_y, camera_z)
    camera_tilt = (camera_tilt_x, camera_tilt_y, camera_tilt_z)

    #camera location array
    def cameraCoords(self):
        return self.camera_coords

    #camera tilt array
    def cameraTilt(self):
        return self.camera_tilt

    def __init__(self):
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

        gluPerspective(90, (display[0]/display[1]), 0.1, 50.0) # (FOV, Resolution, NearClippingPlane, FarClippingPlane)
        
        glTranslatef(0.0, 0.0, -10) # (x, y, z)

        #glRotatef(25, 5, 5, 5)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Camera Works
        camera = glGetDoublev(GL_MODELVIEW_MATRIX)
        
        self.camera_x = camera[3][0]
        self.camera_y = camera[3][1]
        self.camera_z = camera[3][2]

        glTranslatef(self.x_move, self.y_move, self.z_move)

        pygame.display.flip()
        pygame.time.wait(16) # in milisecs

    # Render Cube
    def renderCube(new_verts, surfaces, edges):

        glBegin(GL_QUADS)

        for surface in surfaces:
            for vertex in surface:
                # glColor3fv(self.colours[2])
                glVertex3fv(new_verts[vertex])

        glEnd()

        glBegin(GL_LINES)

        for edge in edges:
            for vertex in edge:
                # glColor3fv(self.colours[4])
                glVertex3fv(new_verts[vertex])

        glEnd()