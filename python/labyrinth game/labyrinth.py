import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640,480])
pygame.display.set_caption("Seiklusmäng")

pilt = pygame.image.load("taust.png")
laius = pilt.get_width()
kõrgus = pilt.get_height()

screen = pygame.display.set_mode([laius, kõrgus])
screen.blit(pilt, [0, 0])

pygame.mouse.set_pos([5,379])
pygame.display.flip()

while True:
    hiire_x, hiire_y = pygame.mouse.get_pos()
    if (hiire_x > 0 and hiire_y > 0):
        clr = screen.get_at((hiire_x, hiire_y))
        if (clr == (0, 0, 0, 255)):
            print("Game over")
            exit()
        if(clr == (255, 0, 0, 255)):
            print("Tubli")
            exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
