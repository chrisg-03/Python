import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Navigation
x = 250
y = 250
w_obj = 100
h_obj = 100
vel = 100

run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False

    pygame.draw.rect(screen, (255, 255, 255), (250, 150, 100, 100), 1)
    pygame.draw.rect(screen, (255, 255, 255), (350, 150, 100, 100), 1)
    pygame.draw.rect(screen, (255, 255, 255), (450, 150, 100, 100), 1)
    pygame.draw.rect(screen, (255, 255, 255), (250, 250, 100, 100), 1)
    pygame.draw.rect(screen, (255, 255, 255), (250, 350, 100, 100), 1)
    pygame.draw.rect(screen, (255, 255, 255), (350, 250, 100, 100), 1)
    pygame.draw.rect(screen, (255, 255, 255), (350, 350, 100, 100), 1)
    pygame.draw.rect(screen, (255, 255, 255), (450, 250, 100, 100), 1)
    pygame.draw.rect(screen, (255, 255, 255), (450, 350, 100, 100), 1)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
        
    pygame.draw.rect(screen, (255, 255, 255), (350, 250, 100, 100))

    pygame.display.update()
pygame.quit() 