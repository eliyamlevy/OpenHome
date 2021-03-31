#!/usr/bin/python

from phue import Bridge
# import logging
# logging.basicConfig()

class switch:

    def __init__(self):
        self.b = Bridge('10.0.0.122')
        self.set_color()
        self.off()


    def on(self):
        self.b.set_light(3, 'on', True)

    def off(self):
        self.b.set_light(3, 'on', False)

    def brighten(self):
        self.b.set_light(3, 'bri', 254) # 254 = max lumens

    def dim(self):
        self.b.set_light(3, 'bri', 100)

    def set_color(self, color=0):
        '''
            color = num in interval [0, 3]
                0 = warm white
                1 = red
                2 = blue
                3 = green
        '''

        xy = [0.4835, 0.4144] # default warm white
        if color == 1:
            # red
            xy = [0.645, 0.3433]
        elif color == 2:
            # blue
            xy = [0.11, 0.11]
        elif color == 3:
            # green
            xy = [0.3, 0.65]
        
        self.b.set_light(3, 'xy', xy)
