import pygame
pygame.init()
screen=pygame.display.set_mode((600,400))

    





image = pygame.image.load("ship.bmp") 
while True:
    screen.fill((230,230,230))
    screen.blit(image,image.get_rect())
    pygame.display.flip()