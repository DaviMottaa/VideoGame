import sys
import pygame

pygame.init()
tamanho_da_tela = (1200,800)
screen=pygame.display.set_mode(tamanho_da_tela)

image = pygame.image.load("ship.bmp") 
ship_rect = image.get_rect()
right_down = False
left_down = False 
ship_rect.bottom = tamanho_da_tela[1]
ship_rect.left = 300

while True:
    #print(str(ship_rect.left)+str(left_down))
    print(True and False)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right_down = True
            if event.key == pygame.K_LEFT:
                left_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right_down = False
            if event.key == pygame.K_LEFT:
                left_down = False
    if right_down and ship_rect.right < tamanho_da_tela[0]:
        ship_rect.centerx += 1
    if left_down and ship_rect.left > 0:
        ship_rect.centerx -= 1
    screen.fill((230,230,230))
    screen.blit(image,ship_rect)
    pygame.display.flip()


