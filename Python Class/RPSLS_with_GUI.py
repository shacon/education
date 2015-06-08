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

def winner_message(choice1, choice2):  
    #returns the appropriate message for the given winner
    winner = find_winner(choice1, choice2)
    if winner == 1:
        message = "Computer chose " + choice_to_str(comp_choice) + ". You won."
    elif winner == 2:
        message = "Computer chose " + choice_to_str(comp_choice) + ". Computer wins!"
    else:
        message = "Computer chose " + choice_to_str(comp_choice) + ". Its a tie!" 
    return message  

def print_message(player_choice): 
    global message
    message = winner_message(player_choice, comp_choice) 

def rock():
    print_message(0)

def paper():
    print_message(1)       

def scissors():
    print_message(2)   

def lizard():
    print_message(3) 

def Spock():
    print_message(4)  

           
            
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