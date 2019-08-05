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
background_image = pygame.image.load("Red Arcade Machine.gif")


while( running ):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Refresh the background image
    screen.blit(background_image, [0, 0])
   
    

    pygame.display.flip()
    clock.tick(clock_tick_rate)

pygame.quit()
