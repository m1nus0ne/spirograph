import sys

import pygame.display

from config import *
from point import point

clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), )
isRunning = True

# init center_dot
center_dot = point(current_cord=(WIN_HEIGHT // 2, WIN_WIDTH // 2))
# init gear_dot
gear_dot = point(previous_cord=(center_dot.current_cord[0] + (WORKSPACE_RADIUS - GEAR_RADIUS),
                                center_dot.current_cord[1]),

                 track_center=center_dot.current_cord, track_radius=WORKSPACE_RADIUS - GEAR_RADIUS
                 , angle_velocity=GEAR_ANGLE_VELOCITY)
gear_dot.current_cord = gear_dot.previous_cord
# init draw_dot
draw_dot = point(previous_cord=(
center_dot.current_cord[0] + WORKSPACE_RADIUS + DOT_RADIUS - GEAR_RADIUS, center_dot.current_cord[1]),

                 track_radius=DOT_RADIUS, track_center=gear_dot.current_cord,
                 angle_velocity=-DOT_ANGLE_VELOCITY)
draw_dot.current_cord = draw_dot.previous_cord
sc.fill(BLACK)
pygame.draw.circle(sc,WHITE,center_dot.current_cord,WORKSPACE_RADIUS+DOT_RADIUS-GEAR_RADIUS,2)

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            sys.exit()

    t = clock.tick(FPS)
    draw_dot.center_update(gear_dot.current_cord)
    gear_dot.move(t)
    draw_dot.move(t)
    draw_dot.draw()
    pygame.display.flip()

