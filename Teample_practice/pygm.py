import pygame
pygame.init()

size = [1000, 700]
screen = pygame.display.set_mode(size)

title = "My Game"
pygame.display.set_caption(title)

clock = pygame.time.Clock()
color = (0, 0, 0)
ss = pygame.image.load("C:/Users/user/Desktop/Omok_Image/Omok_image.png").convert_alpha()
ss = pygame.transform.scale(ss, (850, 700))

SB = 0
while SB == 0:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1

    screen.fill(color)
    screen.blit(ss, (0, 0))
    pygame.display.flip()




pygame.quit()



