import pyglet

class Planet(pyglet.sprite.Sprite):
    def __init__(self, image, x=0, y=0, batch=None):
        super(Planet, self).__init__(
                                     image, x, y, batch=batch)
        self.x = x
        self.y = y

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