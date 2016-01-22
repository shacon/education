

# for Coursera Class in Interactive Python
# with professors Joe Warren, Scott Rixner, John Greiner, Stephen Wong at Rice University
# art assets created by Kim Lathrop
# works best on Chrome/Chromium web browser (with Codeskulptor)
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
started = False
rock_group = set([])
missile_group = set([])
explosion_group = set([])

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40, 500)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.thruster = False
        self.friction = .04
        forward = angle_to_vector(self.angle)

    def draw(self,canvas):
       canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        for i in range(2):
            self.angle += self.angle_vel
            self.pos[i] += self.vel[i]
            self.vel[i] *= (1 -self.friction)
        if self.thruster:
            ang = angle_to_vector(self.angle)
            for i in range(2):
                self.vel[i] += (ang[i] * .8)
                self.pos[i] += self.vel[i]
        if self.pos[0] > WIDTH or self.pos[0] < 0:
            self.pos[0] = self.pos[0] % WIDTH
        if self.pos[1] > HEIGHT or self.pos[1] < 0:
            self.pos[1] = self.pos[1] % HEIGHT


    def turn_left(self):
        self.angle_vel -= .04

    def turn_right(self):
        self.angle_vel += .04

    def stop_turn(self):
        self.angle_vel = 0

    def stop_thrust(self):
        self.thruster = False
        self.image_center = [45, 45]
        ship_thrust_sound.pause()
        ship_thrust_sound.rewind()

    def start_thrust(self):
        self.thruster = True
        self.image_center = [135, 45]
        ship_thrust_sound.play()

    def fire_missile(self):
        global missile_group
        ang = angle_to_vector(self.angle)
        pos = [self.pos[0] + (ang[0] * 45), self.pos[1] + (ang[1] * 45)]
        a_missile = Sprite(pos, [self.vel[0] + (ang[0] *6), self.vel[1] + (ang[1]*6)], 0, 0, missile_image, missile_info, missile_sound)
        missile_group.add(a_missile)


# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def draw(self, canvas):

        if self.animated:
            x_pos = self.age * self.image_center[0]
            canvas.draw_image(self.image, [x_pos, self.image_center[1]], self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.angle += self.angle_vel
        self.age += 1
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        if self.age < self.lifespan:
            return False
        else:
            return True

    def collide(self, other_object):
        if dist(self.pos, other_object.pos) <= self.radius + other_object.radius:
            return True
        else:
            return False

def keydown_handler(key):
    keys = {simplegui.KEY_MAP['right']:my_ship.turn_right, simplegui.KEY_MAP['left']:my_ship.turn_left,
            simplegui.KEY_MAP['up']:my_ship.start_thrust, simplegui.KEY_MAP['space']:my_ship.fire_missile}
    for i in keys:
        if i == key:
            keys[i]()

def keyup_handler(key):
    my_ship.stop_turn()
    my_ship.stop_thrust()

#helper functions

def process_sprite_group(sprite_set, canvas):
    for sprite in set(sprite_set):
         if sprite.update() == True:
            sprite_set.remove(sprite)
    for sprite in sprite_set:
        sprite.draw(canvas)
        sprite.update()

def group_collide(group, other_object):
    collision = False
    for sprite in set(group):
        if sprite.collide(other_object):
            group.remove(sprite)
            collision = True
    return collision

def group_group_collide(group1, group2):
    collision_count = 0
    for sprite in set(group1):
        if group_collide(group2, sprite):
            explosion = Sprite(sprite.pos, sprite.vel, sprite.angle, sprite.angle_vel, explosion_image, explosion_info, explosion_sound)
            group1.discard(sprite)
            collision_count += 1
            explosion_group.add(explosion)
    return collision_count

def update_lives():
    global rock_group, lives, started, points, score
    if group_collide(rock_group, my_ship) == True:
        lives -= 1
    if lives == 0:
        started = False
        soundtrack.pause()
        soundtrack.rewind()
        points = 0
        lives = 3
        score = 0




# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        soundtrack.play()

# timer handler that spawns a rock
def rock_spawner():
    global rock_group, started
    pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
    vel = [(random.random() * .6 - .3), (random.random() * .6 - .3)]
    ang = 0
    ang_vel = random.random() * .2 - .1
    image = asteroid_image
    info = asteroid_info
    a_rock = Sprite(pos, vel, ang, ang_vel, image, info, sound = None)
    if len(rock_group) < 12 and started and not a_rock.collide(my_ship):
        rock_group.add(a_rock)

def draw(canvas):
    global time, started, rock_group, lives, missile_group, score
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    update_lives()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_text("SCORE:" + str(score), (20, 30), 30, 'white')
    canvas.draw_text('LIVES:' + str(lives), (20, 70), 30, 'white')
    # draw ship and sprites
    my_ship.draw(canvas)
    process_sprite_group(missile_group, canvas)
    process_sprite_group(rock_group, canvas)
    process_sprite_group(explosion_group, canvas)
    score += group_group_collide(rock_group, missile_group)
    # update ship and sprites
    my_ship.update()

     # draw splash screen if not started
    if not started:

        canvas.draw_image(splash_image, splash_info.get_center(),
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                          splash_info.get_size())
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)

# register handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

timer = simplegui.create_timer(1000.0, rock_spawner)

frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)

#start
timer.start()
frame.start()
