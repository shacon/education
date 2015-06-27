import simplegui
import random



message = "Make your choice"
comp_choice = random.randrange(5)

def which_player_wins(player, value):
    if player == value:
        value = 1
    else:
        value = 2
    return value

def find_winner(player1, player2):
#finds a winnner using modular arithmetic
    abs_diff = abs(player1 - player2) % 5
    if 0 < abs_diff < 3:
    #higher number wins max(1, 2)
        winner = max(player1, player2)
        which_player_wins(player1, player2)
    elif abs_diff > 2:
    #lower number wins
        winner = min(player1, player2)
        which_player_wins(player1, player2)
    else:
        winner = 3
    return winner
    
def choice_to_str(num):
    items = ['rock', 'Spock', 'paper', 'lizard', 'scissors']
    return items[num]

def str_to_choice(name):
    items = { 0 : 'rock', 1 : "Spock",  2 : "paper", 3 : "lizard", 4 : "scissors"}


    
      

# Handlers for mouse click

def create_game_message(winning_player):
    messages = {1 :" You won!", 2 : " Computer wins!", 3 : " It's a tie!"}
    return "Computer chose " + choice_to_str(comp_choice) + "."+ messages[winning_player]
    
def winner_message(choice1, choice2):  
    #returns the appropriate message for the given winner
    winner = find_winner(choice1, choice2)
    message = create_game_message(winner)
    return message

def print_message(player_choice): 
    #tells python that the variable message is global
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
    canvas.draw_text(message, [100,100], 25, "White", "monospace")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 600, 500)
frame.add_button("Rock", rock)
frame.add_button("Spock", paper)
frame.add_button("Paper", scissors)
frame.add_button("Lizard", lizard)
frame.add_button("Scissors", Spock)
frame.set_draw_handler(draw)

# Start the frame animation
frame.set_canvas_background('Teal')
frame.start()