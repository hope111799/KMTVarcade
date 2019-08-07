# import pygame
import pygame

# initialize game engine
pygame.init()

window_width=900
window_height=594

animation_increment=10
clock_tick_rate=20

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("StArcade")

running = True

clock = pygame.time.Clock()
background_image = pygame.image.load("Red_Arcade_Machine.gif")


while( running ):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Refresh the background image
    screen.blit(background_image, [0, 0])
   
    
    red= (255,0,0)
    spinner= pygame.draw.circle(screen, red, (350, 150), 60)
    pygame.display.flip()

    blue= (3,198,252)
    space= pygame.draw.circle(screen, blue, (550, 150), 60)
    pygame.display.flip()

    yellow= (252,248,3)
    pacman= pygame.draw.circle(screen, yellow, (440, 300), 60)
    pygame.display.flip()

pygame.quit()
