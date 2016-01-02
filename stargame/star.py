import pyglet
from pyglet.window.key import modifiers_string
from pyglet.window import key
import math
from django.template.defaulttags import widthratio

window = pyglet.window.Window(fullscreen=True)
pyglet.resource.path.append('./images')
pyglet.resource.reindex()

def center_anchor(img):
    img.anchor_x = img.width//2
    img.anchor_y = img.height//2


planet_image = pyglet.resource.image('tn-p_lorri_fullframe_color.jpg')
center_anchor(planet_image)

ship_image = pyglet.resource.image('shipanim_off.jpg')
center_anchor(ship_image)

ship_image_on = pyglet.resource.image('shipanim_on.jpg')
center_anchor(ship_image_on)

def update(dt):
    print "ship.update,dt:", dt
    ship.update(dt)
    planet.update(dt)


class Planet(pyglet.sprite.Sprite):
    def __init__(self, image, x=0, y=0, batch=None):
        super(Planet, self).__init__(
                                     image, x, y, batch=batch)
        self.x = x
        self.y = y
        self.mass = 5000000 # experiment!
        
    def dist_vec_to(self, target):
        dx = target.x -self.x
        dy = target.y - self.y
        sqr_distance = dx**2 + dy**2
        distance = math.sqrt(sqr_distance)
        
        angle = math.acos(float(dx)/distance)
        if dy < 0:
            angle = 2*math.pi - angle
        return (distance, angle)
    
    def force_on(self, target):
        G = 1 # expriment!
        distance, angle = self.dist_vec_to(target)
        return ((-G * self.mass)/(distance**2), angle)
        
    def update(self, dt):
        force, angle = self.force_on(ship)
        force_x = force * math.cos(angle) * dt
        force_y = force * math.sin(angle) * dt
        ship.dx += force_x
        ship.dy += force_y

class Ship(pyglet.sprite.Sprite):
    def __init__(self, image, x=0, y=0, 
                 dx=0, dy=0, rotv=0, batch=None):
        super(Ship, self).__init__(
                                   image, x, y, batch=batch)
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rotation = rotv
        self.thrust = 200.0
        self.rot_spd = 100.0
        self.rot_left = False
        self.rot_right = False
        self.engines = False
    
    def update(self, dt):
        self.image = ship_image        
        if self.rot_left:
            self.rotation -= self.rot_spd*dt
            print "rot_left, self.rotation:", self.rotation
        if self.rot_right:
            self.rotation += self.rot_spd*dt
            print "rot_right, self.rotation:", self.rotation
        self.rotation = wrap(self.rotation, 360.)
        if self.engines:
            self.image = ship_image_on
            rotation_x = math.cos(
                                  to_radians(self.rotation))
            rotation_y = math.sin(
                                  to_radians(-self.rotation))
            self.dx += self.thrust * rotation_x * dt
            self.dy += self.thrust * rotation_y * dt
            
        self.x += self.dx * dt
        self.y += self.dy * dt
        self.x = wrap(self.x, window.width)
        self.y = wrap(self.y, window.height)
            
                
def wrap(value, width):
    if width == 0:
        return 0
    if value > width:
        value -= width
    if value < 0:
        value += width
    return value


def to_radians(degrees):
    return math.pi * degrees / 180.0

center_x = int(window.width/2)
center_y = int(window.height/2)
planet = Planet(planet_image, center_x, center_y, None)
ship = Ship(ship_image, center_x+500, center_y, dx=0, dy=150, rotv=0)

pyglet.clock.schedule_interval(update, 1/60.0)

@window.event
def on_draw():
    window.clear()
    planet.draw()
    ship.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        print "ship.rot_left = True"
        ship.rot_left = True
    if symbol == key.RIGHT:
        print "ship.rot_right = True"
        ship.rot_right = True
    if symbol == key.UP:
        print "ship.engines = True"
        ship.engines = True

@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.LEFT:
        print "ship.rot_left = False"
        ship.rot_left = False
    if symbol == key.RIGHT:
        print "ship.rot_right = False"
        ship.rot_right = False
    if symbol == key.UP:
        print "ship.engines = False"
        ship.engines = False        
        
pyglet.app.run()

    
    
