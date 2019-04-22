import random
import os
import time

from pygame import *
import pygame
import math

WIDTH = HEIGHT = 400
DISPLAY = (WIDTH, HEIGHT)
FPS = 30
RUNNING = True
FONT = "monospace"

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

POINT_RADIUS = 5

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode(DISPLAY)

pygame.display.set_caption("Dude")
clock = pygame.time.Clock()
point_img = pygame.image.load(os.path.join(os.path.dirname(__file__), 'img/point.png')).convert()
bg_img = pygame.image.load(os.path.join(os.path.dirname(__file__), 'img/bg.png')).convert()


class Point(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = int(x)
        self.y = int(y)
        self.radius = 2
        self.image = pygame.transform.scale(point_img, (self.radius, self.radius))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        pass

in_c = 0
out_c = 0
point_arr = []

point_group = pygame.sprite.Group()
m = 1
time.delay(10000)
while RUNNING:
    clock.tick(250)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False


    res = in_c+out_c

    for i in range(m):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        point_arr.append(Point(x, y))
    point_group.add(point_arr)
    point_group.update()

    if x**2+(y - HEIGHT)**2 <= WIDTH**2:
        in_c += 1
    else:
        out_c += 1

    screen.fill(WHITE)
    pygame.draw.circle(screen, GRAY, [0, HEIGHT], WIDTH)
    point_group.draw(screen)
    myfont = pygame.font.SysFont(FONT, 20)
    in_cd = myfont.render(str(in_c), 1, RED)
    screen.blit(in_cd, (WIDTH - 230, 20))
    pygame.draw.line(screen, RED, [WIDTH-170, 40], [WIDTH-230, 40])
    res_cd = myfont.render(str(res), 1, RED)
    screen.blit(res_cd, (WIDTH - 230, 38))
    fourx = myfont.render("4x ", 1, RED)
    screen.blit(fourx, (WIDTH - 265, 30))
    pygame.draw.line(screen, RED, [WIDTH-157, 38], [WIDTH-147, 38])
    pygame.draw.line(screen, RED, [WIDTH-157, 42], [WIDTH-147, 42])
    pi_cd = myfont.render(str(float(4*((in_c+1)/(res+1))))[:7], 1, RED)
    screen.blit(pi_cd, (WIDTH - 144, 29))
    pygame.display.flip()

    if float(str(float(4 * ((in_c + 1) / (res + 1))))[:7]) == 3.14159:
        time.delay(1000)
        break



pygame.quit()
