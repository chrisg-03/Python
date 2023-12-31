import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False

pygame.quit()