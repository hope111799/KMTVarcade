# import pygame
import pygame
import math

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

   #Creates the buttons
    
    red= (255,0,0)
    box1= (320,150,80,80)
    pygame.draw.rect(screen, red, box1)
    pygame.display.flip()

    blue= (3,198,252)
    box2= (500, 150, 80, 80)
    pygame.draw.rect(screen, blue, box2)
    pygame.display.flip()

    yellow= (252,248,3)
    box3= (410, 300, 80, 80)
    pygame.draw.rect(screen, yellow,box3)
    pygame.display.flip()

###creating the buttons to redirect
##
##clicked= win.checkMouse()
##radius= 60
##Bluemouse_position= win.getMouse() 
##Redmouse_position= 
##Yellowmouse_position=
##
###Blue button redirect
##if Bluemouse_position == < radius: 
##
###Red button redirect
##
###Yellow button redirect
    
    


pygame.quit()
