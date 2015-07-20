# implementation of card game - Memory

import simplegui
import random

class State():
    cards = range(1, 9) + range(1, 9)   
    exposed = []
    x = 25
    click_count = 0
    card1 = 0
    card2 = 0
    turns = 0

s = State()

def init():    
    random.shuffle(s.cards)
    for items in s.cards:
        s.exposed = [False] + s.exposed
     
# helper function to initialize globals
def new_game():
    #reset state
    s.cards = range(1, 9) + range(1, 9)   
    s.exposed = []
    s.x = 25
    s.click_count = 0
    s.card1 = 0
    s.card2 = 0
    s.turns = 0
    init()
    label.set_text("Turns = " + str(s.turns))

def incr_click():
    if s.click_count == 0:
        s.click_count += 1
    elif s.click_count == 1:
        s.click_count += 1
    else:
        s.click_count = 1
        
def activate_card(i):
    if s.click_count == 2:
        if s.cards[s.card1] == s.cards[s.card2]:
            s.card2 = 0
            s.card1 = i
            s.exposed[i] = True
        else:    
            s.exposed[s.card1] = False #flip
            s.exposed[s.card2] = False
            s.card2 = 0
            s.card1 = i 
            s.exposed[i] = True        
        incr_click()      
    elif s.click_count == 1:
        s.exposed[i] = True
        incr_click()
        s.card2 = i
        s.turns += 1
        label.set_text("Turns = " + str(s.turns))
    else:
        s.exposed[i] = True
        incr_click()
        s.card1 = i       
        
# define event handlers
def mouseclick(pos):
    p = pos[0] // 50
    if s.exposed[p] == False:
        activate_card(p)
                            
# cards are logically 50x100 pixels in size    
def draw(canvas):    
    x = 25
    l = range(1, 17)
    counter = 0 
    for item in s.cards:        
            if s.exposed[counter] == True:
                canvas.draw_text(str(item), (x, 50), 20, 'White') 
                x += 50
                counter += 1
            else:
                canvas.draw_image(image, (100, 100), (200, 200), (x, 50), (50, 100))
                x += 50
                counter += 1
        
image = simplegui.load_image('https://placekitten.com/200/200?image=1')
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)

label = frame.add_label('Turns')
label.set_text( "Turns = " + str(s.turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
init()
new_game()
frame.start()