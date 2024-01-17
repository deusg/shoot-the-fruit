from random import randint
import pgzrun

apple = Actor("apple.png") 


def draw():
    screen.clear()
    apple.draw()


def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)


def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()
    else:
        print("You missed. Game Over!")
        quit()


place_apple()
place_apple()
pgzrun.go()
