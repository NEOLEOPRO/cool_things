import pygame, random

#параментры тут
speed = 1200
point = 0, 0

pygame.init()
width, height = 800, 800
x, y = int(width), int(height)
screen = pygame.display.set_mode((x, y))
pygame.display.flip()
pygame.display.set_caption('Fractal fern')
clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.rect(screen, (255, 255, 255), (((point[0]) * x / 5 + 360, y - point[1] * y / 10 + 20), (1, 1)))
    rand = random.random()
    if rand <= 0.01:
        point = 0, 0.16 * point[1]
    elif rand > 0.01 and rand <= 0.86:
        point = 0.85 * point[0] + 0.04 * point[1], -0.04 * point[0] + 0.85 * point[1] + 1.6
    elif rand > 0.86 and rand <= 0.93:
        point = 0.20 * point[0] - 0.26 * point[1], 0.23 * point[0] + 0.22 * point[1] + 1.6
    elif rand > 0.95 and rand <= 1.00:
        point = -0.15 * point[0] + 0.28 * point[1], 0.26 * point[0] + 0.24 * point[1] + 0.44
    pygame.display.update()
    pygame.display.flip()
    clock.tick(speed)
pygame.quit()
