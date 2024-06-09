import pygame
from random import randint

pygame.init()

W,H = 800,500
sc = pygame.display.set_mode((800,500))
pygame.display.set_caption("Pilt")

pygame.draw.rect(sc,(25, 48, 20),(0,420,800,500))
pygame.draw.rect(sc,(17, 15, 54),(0,0,800,420))
lsx = [randint(0, 800) for i in range(100)]
lsy = [randint(0, 400) for i in range(100)]
for i in range(len(lsx)):
    pygame.draw.circle(sc, (255, 223, 200), (lsx[i],lsy[i]),1)
pygame.draw.circle(sc, (255, 223, 200),(650,100),25)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()