# ------- START ATTRIBUTED CODE SECTION -------
# Code created with the help of Grant Jenks
# http://www.grantjenks.com/docs/freegames/fidget.html
# --------- END ATTRIBUTED CODE SECTION --------
import pygame
from turtle import *
def main():
    pygame.mixer.init() 

    pygame.mixer.music.load("arcademusic.mp3")

    pygame.mixer.music.play(1)
    
    state = {'turn': 0}

    def spinner():
        "Make fidget spinner."
        clear()
        angle = state['turn'] / 10
        right(angle)
        forward(100)
        dot(170, 'cyan')
        back(100)
        right(120)
        forward(100)
        dot(170, 'hot pink')
        back(100)
        right(120)
        forward(100)
        dot(170, 'magenta')
        back(100)
        right(120)
        update()

    def animate():
        "Animate fidget spinner."
        if state['turn'] > 0:
            state['turn'] -= 1

        spinner()
        ontimer(animate, 20)
     
    def flick():
        "Flick fidget spinner."
        state['turn'] += 10

    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    width(20)
    onkey(flick, 'space')
    listen()
    animate()
    done()

if __name__== "__main__":
    main()




