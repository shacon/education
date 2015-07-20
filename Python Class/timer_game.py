# timer interval .1 secs
# event handler increments global int  create timee takes ms
# start 
# stop buttons
# then add reset button

# opens frame with stopwatch stopped
import simplegui

#initialize globale variables
timer_num = 0
watch_stopped = 0
stopped_success = 0 

#handlers and game logic
def update_timer():
    global timer_num
    timer_num += 1
      
def start():
    #starts the game
    timer.start()

def two_person():
    #changes the game to two person
    pass

def stop():
    global watch_stopped, timer_num, stopped_success
    watch_stopped += 1
    if timer_num % 10 == 0:
        stopped_success += 1
    timer.stop()

def reset():
    global timer_num, watch_stopped, stopped_success
    timer.stop()
    timer_num = 0
    watch_stopped = 0
    stopped_success = 0 

def draw_current_time(canvas):
    canvas.draw_text(str(stopped_success) + "/" + str(watch_stopped), (400, 50), 20, 'Fuchsia') 
    canvas.draw_text(str(format(timer_num)), (200, 200), 50, 'Orange')
    
#-------------helper functions----------
def format(num):
	#puts seconds in form A:BC.D
    d = num % 10
    c = num % 100 / 10
    b = (num / 100) % 6
    a = num / 600
    return str(a) + ":" + str(b) + str(c) + "." + str(d)

#-------------Frame--------------------

frame = simplegui.create_frame('The Timer Game', 500, 500)

#-------------Canvas--------------------
frame.set_draw_handler(draw_current_time)
frame.set_canvas_background('Teal')

#-------------Control Objects-------------------
#labels
frame.add_label('The Timer Game')
frame.add_label('    ')
frame.add_label('Try to hit stop at each whole second')
#buttons
frame.add_button('Start', start)
frame.add_button('Stop', stop)
frame.add_button('Reset', reset)

#creates timer-must convert 0.1 seconds to milliseconds
timer = simplegui.create_timer(100, update_timer)

frame.start()