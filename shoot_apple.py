from random import randint, choice
import pgzrun

apple = Actor("apple.png") 
orange = Actor("orange.png")
apple_clicks = 0


def draw():
    screen.clear()
    apple.draw()
    orange.draw()


def place_actor(actor):
    actor.x = randint(10, 800)
    actor.y = randint(10, 600)

def place_objects():
    chosen_actor = choice([apple, orange])
    place_actor(chosen_actor)


def on_mouse_down(pos):
    global apple_clicks, total_attempts
    if apple.collidepoint(pos):
        print("Good shot! 🍎")
        apple_clicks += 1
        print(f"Score: {apple_clicks}")
        
    elif orange.collidepoint(pos):
        print("Oops! You clicked 🍊 instead of 🍎")
        apple_clicks -= 1
        print(f"Score: {apple_clicks}")
    else:
        print("You missed. Game Over!")
        print(f"Final Score: {apple_clicks}")
        quit()
    
    place_objects()
    

place_objects()
pgzrun.go()
