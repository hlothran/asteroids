import pygame
from circleshape import *
from constants import *

# Player Class
class Player(CircleShape):
    def __init__(self, x, y):
        self.rotation = 0
        CircleShape(self, x, y, PLAYER_RADIUS)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]