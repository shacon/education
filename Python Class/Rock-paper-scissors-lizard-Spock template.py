import random
def name_to_number(name):
    if name == 'rock':
        name = 0
    elif name == 'Spock':
        name = 1
    elif name == 'paper':
        name = 2
    elif name == 'lizard':
        name = 3
    else:
        name = 4
    return name

def number_to_name(number):
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    else:
        name = 'scissors'
    return name

def rpsls(player_choice): 
    print "    "
    print "Player chooses " + player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice
    # compute difference of comp_number and player_number modulo five
    abs_diff = abs(comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    if 0 < abs_diff < 3:
        #higher number wins max(1, 2)
        winner = max(comp_number, player_number)
        if comp_number == winner:
            print "Computer wins!"
        else:
            print "Player wins!"
    elif abs_diff > 2:
        #lower number wins
        winner = min(comp_number, player_number)
        if comp_number == winner:
            print "Computer wins!"
        else:
            print "Player wins!"
    else:
        print "Player and computer tie!"
rpsls('rock')   
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


