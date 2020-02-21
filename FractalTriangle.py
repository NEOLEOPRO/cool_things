import pygame, random

#параментры тут
length, points, speed = 2, ((20, 20), (780, 20), (400, 780)), 1200
xp, yp = 20, 20

pygame.init()
width, height = 800, 800
x, y = int(width), int(height)
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('Fractal triangle')
pygame.display.flip()
clock = pygame.time.Clock()
for i in points:
    pygame.draw.rect(screen, (255, 255, 255), (i, (1, 1)))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    point = random.choice(points)
    pygame.draw.rect(screen, (255, 255, 255), ((xp, yp), (1, 1)))
    xp, yp = (xp + point[0]) // length, (yp + point[1]) // length
    pygame.display.update()
    pygame.display.flip()
    clock.tick(speed)
pygame.quit()
