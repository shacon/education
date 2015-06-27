#the classic arcade game pong
#from Introduction to Interactive Programming in Python Course by Joe Warren, Scott Rixner, 
#John Greiner, Stephen Won at Rice University
#for a live demo of this game, go to http://www.codeskulptor.org/#user40_olDBDd9182_0.py

import simplegui
import random

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

class State:
    #holds the values that reflect the game's state
    ball_pos = [(WIDTH / 2), HEIGHT / 2]
    ball_vel = [0, 0]
    paddle1_vel = [0, 0]
    paddle2_vel = [0, 0]
    wait_time = 0
    paddle1_ypos = [((HEIGHT / 2) - HALF_PAD_HEIGHT), ((HEIGHT / 2) - HALF_PAD_HEIGHT), ((HEIGHT / 2) + HALF_PAD_HEIGHT), ((HEIGHT / 2) + HALF_PAD_HEIGHT)]
    paddle1_xpos = [0, PAD_WIDTH, PAD_WIDTH, 0]
    paddle2_ypos = [((HEIGHT / 2) - HALF_PAD_HEIGHT), ((HEIGHT / 2) - HALF_PAD_HEIGHT), ((HEIGHT / 2) + HALF_PAD_HEIGHT), ((HEIGHT / 2) + HALF_PAD_HEIGHT) ]
    paddle2_xpos = [WIDTH,(WIDTH - PAD_WIDTH), (WIDTH - PAD_WIDTH), WIDTH ]
    score1 = 0
    score2 = 0
s = State()

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):#(direction):    
    s.ball_pos = [(WIDTH / 2), HEIGHT / 2]
    if direction == False:
        s.ball_vel = [random.randrange(-3, -1), random.randrange(-3, -1)]
    elif direction == True:
        s.ball_vel = [random.randrange(1, 3), random.randrange(-3, -1)]
    else:
        s.ball_vel = [random.randrange(3, 1), random.randrange(-1, -3)]
    update_ball()
                      
# define event handlers
def new_game():    
    s.score1 = 0
    s.score2 = 0
    r = [LEFT, RIGHT]
    spawn_ball(r[random.randrange(0,2)])
        
def draw(canvas):  
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_circle([s.ball_pos[0], s.ball_pos[1]], BALL_RADIUS, 20,  'Teal', 'Teal')
    canvas.draw_polygon([[s.paddle1_xpos[0], s.paddle1_ypos[0]], [s.paddle1_xpos[1],  s.paddle1_ypos[1]], [s.paddle1_xpos[2],  s.paddle1_ypos[2]], [s.paddle1_xpos[3],  s.paddle1_ypos[3]]], 5, 'Brown', 'White')
    canvas.draw_polygon([[s.paddle2_xpos[0], s.paddle2_ypos[0]], [s.paddle2_xpos[1],  s.paddle2_ypos[1]], [s.paddle2_xpos[2],  s.paddle2_ypos[2]], [s.paddle2_xpos[3],  s.paddle2_ypos[3]]], 5, 'Brown', 'White')
    canvas.draw_text(str(s.score1), (80, 50), 25, 'Navy', 'sans-serif')
    canvas.draw_text(str(s.score2), (450, 50), 25, 'Navy', 'sans-serif')
    update_ball()
    update_paddles()
    bounce()
   
def bounce():
    global BALL_RADIUS, HEIGHT, PAD_WIDTH, WIDTH
    pad1_y_range = range(s.paddle1_ypos[0], s.paddle1_ypos[2])
    pad2_y_range = range(s.paddle2_ypos[0], s.paddle2_ypos[2]) 
    if s.ball_pos[1] <= BALL_RADIUS:
        wall_bounce()
    elif s.ball_pos[1] > (HEIGHT - BALL_RADIUS):
        wall_bounce()
    #ball goes into gutter or hits right paddle    
    elif int(s.ball_pos[0]) >= ((WIDTH - PAD_WIDTH) - BALL_RADIUS):
        #check to see if ball has hit right paddle
        if int(s.ball_pos[1]) in pad2_y_range:
            paddle_bounce()
            s.ball_vel[1] = s.ball_vel[1] + ((s.ball_vel[1]) * .05)
            s.ball_vel[0] = s.ball_vel[0] + ((s.ball_vel[0]) * .05)
        else:
            s.score1 += 1
            spawn_ball(LEFT)
    #test to see whether ball is hitting left gutter or left paddle
    elif int(s.ball_pos[0]) <= (PAD_WIDTH + BALL_RADIUS):
        if int(s.ball_pos[1]) in pad1_y_range:
            paddle_bounce()
            s.ball_vel[1] = s.ball_vel[1] + ((s.ball_vel[1]) * .05)
            s.ball_vel[0] = s.ball_vel[0] + ((s.ball_vel[0]) * .05)
        else:
            s.score2 += 1
            spawn_ball(RIGHT)
        
def update_paddles():
    #updates the location of the paddles 
    #must check what the update will produce then decide whether to update
    if (s.paddle1_ypos[0] + s.paddle1_vel[0]) >= 0 and ((s.paddle1_ypos[2] + s.paddle1_vel[0]) < HEIGHT):     
        s.paddle1_ypos[:] = [i + s.paddle1_vel[0] for i in s.paddle1_ypos] 
    if (s.paddle2_ypos[0] + s.paddle2_vel[0]) >= 0 and ((s.paddle2_ypos[2] + s.paddle2_vel[0]) < HEIGHT):        
        s.paddle2_ypos[:] = [i + s.paddle2_vel[0] for i in s.paddle2_ypos]
  
def update_ball():
    s.ball_pos[0] += s.ball_vel[0]
    s.ball_pos[1] += s.ball_vel[1]

def paddle_bounce():
    s.ball_vel[0] = -(s.ball_vel[0])
     
def wall_bounce():
    s.ball_vel[1] = -(s.ball_vel[1])
    
def timer():
    s.wait_time += 1
    if s.wait_time == 10:
        timer.stop()
        new_game()
          
def keydown(key):
    if key == simplegui.KEY_MAP["S"]:
        s.paddle1_vel[:] = [i + 5 for i in s.paddle1_vel]
    elif key == simplegui.KEY_MAP["W"]:
        s.paddle1_vel[:] = [i - 5 for i in s.paddle1_vel]
    elif key == simplegui.KEY_MAP["down"]:
        s.paddle2_vel[:] = [i + 5 for i in s.paddle2_vel]
    elif key == simplegui.KEY_MAP["up"]:
        s.paddle2_vel[:] = [i - 5 for i in s.paddle2_vel]
    
def keyup(key):
    if key == simplegui.KEY_MAP["S"]:
        s.paddle1_vel[:] = [0, 0]
    elif key == simplegui.KEY_MAP["W"]:
        s.paddle1_vel[:] = [0, 0]
    elif key == simplegui.KEY_MAP["down"]:
        s.paddle2_vel[:] = [0, 0]
    elif key == simplegui.KEY_MAP["up"]:
        s.paddle2_vel[:] = [0, 0]

#---button handler        
def restart_button():
    new_game()
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_canvas_background('Orange')
frame.set_keydown_handler(keydown)
button1 = frame.add_button('Restart', restart_button, 50)
timer = simplegui.create_timer(100, timer)

frame.start()
timer.start()
