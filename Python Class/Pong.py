# Implementation of classic arcade game Pong

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [(WIDTH / 2), HEIGHT / 2]
ball_vel = [10, 1]
paddle1_ypos = [((HEIGHT / 2) - HALF_PAD_HEIGHT), ((HEIGHT / 2) - HALF_PAD_HEIGHT), ((HEIGHT / 2) + HALF_PAD_HEIGHT), ((HEIGHT / 2) + HALF_PAD_HEIGHT)]
paddle1_xpos = [0, PAD_WIDTH, PAD_WIDTH, 0]
paddle2_ypos = [((HEIGHT / 2) - HALF_PAD_HEIGHT), ((HEIGHT / 2) - HALF_PAD_HEIGHT), ((HEIGHT / 2) + HALF_PAD_HEIGHT), ((HEIGHT / 2) + HALF_PAD_HEIGHT) ]
paddle2_xpos = [WIDTH,(WIDTH - PAD_WIDTH), (WIDTH - PAD_WIDTH), WIDTH ]

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):#(direction):
    global ball_pos, ball_vel, seconds # these are vectors stored as lists
   
    ball_pos = [(WIDTH / 2), HEIGHT / 2]
    print 'change ball pos'
    if direction == False:
        ball_vel = [random.randrange(-8, -4), random.randrange(-5, -3)]
        print 'LEFT'
    elif direction == True:
        ball_vel = [random.randrange(6, 10), random.randrange(-5, -3)]
        print 'RIGHT'
    update_ball()
     


  
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(' ')
    
   

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel    
    # draw mid line and gutters

    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_circle([ball_pos[0], ball_pos[1]], BALL_RADIUS, 10, 'Peach', 'Yellow')
    canvas.draw_polygon([[paddle1_xpos[0], paddle1_ypos[0]], [paddle1_xpos[1],  paddle1_ypos[1]], [paddle1_xpos[2],  paddle1_ypos[2]], [paddle1_xpos[3],  paddle1_ypos[3]]], 5, 'Brown', 'White')
    canvas.draw_polygon([[paddle2_xpos[0], paddle2_ypos[0]], [paddle2_xpos[1],  paddle2_ypos[1]], [paddle2_xpos[2],  paddle2_ypos[2]], [paddle2_xpos[3],  paddle2_ypos[3]]], 5, 'Brown', 'White')
    update_ball()

    bounce()
   
    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    
    # determine whether paddle and ball collide    
    
    # draw scores
def update_ball():
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
def keydown(key):
    global paddle1_vel, paddle2_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
def reverse_vel():
    ball_vel[0] = -(ball_vel[0])
    ball_vel[1] = -(ball_vel[1])
    
def paddle_up(pad_y_cords):
    pad_y_cords[:]=[i-10 for i in pad_y_cords]
    print 'paddleup'
    
def paddle_down(pad_y_cords):
    pad_y_cords[:]=[i+10 for i in pad_y_cords]
    print 'paddledown'
    

    
def bounce():
    global ball_pos, BALL_RADIUS, HEIGHT
    pad1_y_range = range(paddle1_ypos[1], paddle1_ypos[2])
    pad2_y_range = range(paddle2_ypos[0], paddle2_ypos[2])
    if ball_pos[1] < BALL_RADIUS:
        reverse_vel()
    elif ball_pos[1] > (HEIGHT - 20):
        reverse_vel()   
    elif ball_pos[0] > WIDTH - PAD_WIDTH:
        if ball_pos[1] in pad1_y_range:
            reverse_vel()
        else:
            spawn_ball(LEFT)
        print pad1_y_range
        print pad2_y_range
        print ball_pos[1]
        print ball_pos[1] in pad1_y_range
    elif ball_pos[0] < PAD_WIDTH:
        if ball_pos[1] in pad2_y_range:
            reverse_vel()
            print 'other gutter'
        else:
            spawn_ball(RIGHT)
        print 'there'

def keydown(key):
    #vel = 4
    global paddle1_ypos, paddle2_ypos
    if key == simplegui.KEY_MAP["S"]:
        paddle_down(paddle1_ypos)
    elif key == simplegui.KEY_MAP["W"]:
        paddle_up(paddle1_ypos) 
    elif key == simplegui.KEY_MAP["down"]:
        paddle_down(paddle2_ypos)
    elif key == simplegui.KEY_MAP["up"]:
        paddle_up(paddle2_ypos)
    
    
        

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_canvas_background('Green')
frame.set_keydown_handler(keydown)


# start frame
new_game()
frame.start()
