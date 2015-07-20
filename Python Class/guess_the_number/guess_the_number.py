
import simplegui
import random
import math
 
range = 100
secret_number = random.randrange(range)
rem_guesses = 7

 #helper function to start and restart the game
def new_game():
    # initialize global variables 
    global range, secret_number, guess, rem_guesses
    guess = None
    if range == 100:
        rem_guesses = 7
    else:
        rem_guesses = 10
    game_greeting()
    input_guess(guess)
  
    
def game_greeting():
    global range, rem_guesses
    print "New game. Range is from 0 to " + str(range)
    print "Number of remaining guesses is " + str(rem_guesses)
    print "   "
   
# define event handlers for control panel
def range_100():
    # button that changes the range to [0,100) and starts a new game 
    global range, secret_number, rem_guesses
    rem_guesses = 7
    range = 100
    secret_number = random.randrange(100)
    new_game()
      
def range_1000():  
    global range, secret_number, rem_guesses 
    range = 1000
    rem_guesses = 10
    secret_number = random.randrange(1000)
    new_game()

def chosen_number():
    global secret_number 
    secret_number = random.randrange(range)
    
def remaining_guesses():
    #returns the number of remaining guesses minus one
    global rem_guesses
    rem_guesses -= 1
    return rem_guesses
        
def input_guess(inp):
    global number, guess, secret_number, range, rem_guesses
    guess = inp
    if guess == None:
        pass
    else:
        remaining_guesses()
        guess = int(guess)
        if secret_number == guess:
            print "Guess was " + str(guess) 
            print "Number of remaining guesses is " + str(rem_guesses)
            print "Correct!"
            print "    "
            new_game()
        elif secret_number > guess and rem_guesses > 0:   
            print "Guess was " + str(guess) 
            print "Number of remaining guesses is " + str(rem_guesses) 
            print "Higher!"
            print "   "            
        elif secret_number < guess and rem_guesses > 0:           
            print "Guess was " + str(guess) 
            print "Number of remaining guesses is " + str(rem_guesses) 
            print "Lower!"
            print "   "
        else:
            print "Guess was " + str(guess) 
            print "Number of remaining guesses is " + str(rem_guesses) 
            print "You ran out of guesses. The number was " + str(secret_number)
            print "   "
          
            new_game()
# call new_game 
new_game()

f = simplegui.create_frame("Guess the Number",300,300)
f.add_input("Enter guess", input_guess, 100)
f.add_label("Range", 100)
f.add_button("Range: 0 to 100 ", range_100, 100)
f.add_button("Range: 0 to 1000", range_1000, 100)

# register event handlers for control elements and start frame
# 
# def fun(x):
#     return x + 1
# # call new_game 
# new_game()


# always remember to check your completed program against the grading rubric


# class TestStringMethods(unittest.TestCase):

#   def test_upper(self):
#       self.assertEqual('foo'.upper(), 'FOO')

#   def test_isupper(self):
#       self.assertTrue('FOO'.isupper())
#       self.assertFalse('Foo'.isupper())

#   def test_split(self):
#       s = 'hello world'
#       self.assertEqual(s.split(), ['hello', 'world'])
#       # check that s.split fails when the separator is not a string
#       with self.assertRaises(TypeError):
#           s.split(2)