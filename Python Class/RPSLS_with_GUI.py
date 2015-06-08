import simplegui
import random



message = "Make your choice"
comp_choice = random.randrange(5)
def find_winner(player1, player2):
    #finds a winnner using modular arithmetic
    abs_diff = abs(player1 - player2) % 5
    if 0 < abs_diff < 3:
        #higher number wins max(1, 2)
        winner = max(player1, player2)
        if player1 == winner:
            winner = 1
        else:
            winner = 2 
    elif abs_diff > 2:
        #lower number wins
        winner = min(player1, player2)
        if player1 == winner:
            winner = 1
        else:
            winner = 2
    else:
        winner = 3
    return winner
    
def choice_to_str(num):
    items = ['rock', 'Spock', 'paper', 'lizard', 'scissors']
    return items[num]
      

# Handlers for mouse click
def rock():
    global message
    winner = find_winner(0, comp_choice)
    if winner == 1:
        message = "Computer chose " + choice_to_str(comp_choice) + ". You won."
    elif winner == 2:
        message = "Computer chose " + choice_to_str(comp_choice) + ". Computer wins!"
    else:
        message = "Computer chose " + choice_to_str(comp_choice) + ". Its a tie!"              
    
def paper():
    global message
    winner = find_winner(1, comp_choice)
    if winner == 1:
        message = "Computer chose " + choice_to_str(comp_choice) + ". You won."
    elif winner == 2:
        message = "Computer chose " + choice_to_str(comp_choice) + ". Computer wins!"
    else:
        message = "Computer chose " + choice_to_str(comp_choice) + ". Its a tie!"              

def scissors():
    global message
    winner = find_winner(2, comp_choice)
    if winner == 1:
        message = "Computer chose " + choice_to_str(comp_choice) + ". You won."
    elif winner == 2:
        message = "Computer chose " + choice_to_str(comp_choice) + ". Computer wins!"
    else:
        message = "Computer chose " + choice_to_str(comp_choice) + ". Its a tie!"   

def lizard():
    global message
    winner = find_winner(3, comp_choice)
    if winner == 1:
        message = "Computer chose " + choice_to_str(comp_choice) + ". You won."
    elif winner == 2:
        message = "Computer chose " + choice_to_str(comp_choice) + ". Computer wins!"
    else:
        message = "Computer chose " + choice_to_str(comp_choice) + ". Its a tie!"     
        
def Spock():
    global message
    winner = find_winner(4, comp_choice)
    if winner == 1:
        message = "Computer chose " + choice_to_str(comp_choice) + ". You won."
    elif winner == 2:
        message = "Computer chose " + choice_to_str(comp_choice) + ". Computer wins!"
    else:
        message = "Computer chose " + choice_to_str(comp_choice) + ". Its a tie!"              
            
# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [100,100], 25, "Purple")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 600, 500)
frame.add_button("Rock", rock)
frame.add_button("Spock", paper)
frame.add_button("Paper", scissors)
frame.add_button("Lizard", lizard)
frame.add_button("Scissors", Spock)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()