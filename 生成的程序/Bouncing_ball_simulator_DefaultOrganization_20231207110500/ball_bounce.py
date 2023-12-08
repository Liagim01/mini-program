import pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Bounce Simulation")
clock = pygame.time.Clock()
balls = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    for ball in balls:
        ball.update(balls)
        ball.draw(screen)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if balls:
            balls[0].mass += 1
    if keys[pygame.K_DOWN]:
        if balls:
            balls[0].mass -= 1
    pygame.display.flip()
    clock.tick(60)
pygame.quit()