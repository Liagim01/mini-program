import pygame
import random
from ball_bounce import balls
class Ball:
    def __init__(self, id, x, y, radius, color, mass, velocity):
        self.id = id
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.velocity = velocity
    def update(self, balls):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        if self.x - self.radius < 0 or self.x + self.radius > 800:
            self.velocity[0] *= -1
            print("Ball", self.id, "collided with the wall")
        if self.y - self.radius < 0 or self.y + self.radius > 600:
            self.velocity[1] *= -1
            print("Ball", self.id, "collided with the wall")
        for ball in balls:
            if ball.id != self.id:
                dx = self.x - ball.x
                dy = self.y - ball.y
                distance = (dx ** 2 + dy ** 2) ** 0.5
                if distance < self.radius + ball.radius:
                    self.velocity[0] *= -1
                    self.velocity[1] *= -1
                    print("Ball", self.id, "collided with another ball")
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)