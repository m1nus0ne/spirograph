from config import *
from math import cos, sin


class point(object):
    def __init__(self, current_cord=(WIN_HEIGHT/2, WIN_WIDTH/2), previous_cord=(WIN_HEIGHT/2, WIN_WIDTH/2), track_center=(0, 0), width=1, track_radius=1,
                 color=WHITE, angle_velocity=0):
        self.current_cord = current_cord
        self.previous_cord = previous_cord
        self.angle_velocity = angle_velocity
        self.track_center = track_center
        self.width = width
        self.color = color
        self.track_radius = track_radius
        self.t = 0

    def move(self, deltaTime):
        self.t += deltaTime
        self.previous_cord = self.current_cord
        self.current_cord = (self.track_center[0] + self.track_radius * cos(self.angle_velocity * self.t),
                             self.track_center[1] + self.track_radius * sin(self.angle_velocity * self.t))

    def draw(self):
        pygame.draw.aaline(SCREEN, self.color, self.previous_cord, self.current_cord, 4)

    def center_update(self, cord):
        self.track_center = cord
