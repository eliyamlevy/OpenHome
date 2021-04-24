#!/usr/bin/python

from phue import Bridge
import time as t
import sys

sys.tracebacklimit = 0

class switch:

    def __init__(self, ip_address):

        self.valid = True
        api = None

        try:
            self.b = Bridge(ip_address)
            self.b.connect()
            api = self.b.get_api()
        except:
            self.valid = False
            print("Unable to connect to bridge with provided ip address:", ip_address)
        
        if self.valid:
            self.lights = list() # contains ids of all the lights associated with the bridge
            if api is not None:
                for light in api['lights']:
                    self.lights.append(int(light[0]))
                    print(self.lights)
            self.set_color()
            self.off()

    def on(self):
        for light in self.lights:
            self.b.set_light(light, 'on', True)
            self.b.set_light(light, 'xy', [0.4835, 0.4144])
            self.b.set_light(light, 'bri', 254)

    def off(self):
        for light in self.lights:
            self.b.set_light(light, 'on', False)

    def brighten(self):
        api = self.b.get_api()
        curr_lumens = api['lights'][str(self.lights[0])]['state']['bri']
        curr_lumens = int(curr_lumens)
        for light in self.lights:
            self.b.set_light(light, 'bri', min(254, curr_lumens + 100)) # 254 = max lumens

    def dim(self):
        api = self.b.get_api()
        curr_lumens = api['lights'][str(self.lights[0])]['state']['bri']
        curr_lumens = int(curr_lumens)
        for light in self.lights:
            self.b.set_light(light, 'bri', max(0, curr_lumens - 100)) # 254 = max lumens

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
        for light in self.lights:
            self.b.set_light(light, 'xy', xy)

# s = switch('10.0.0.122')
# s.on()
# t.sleep(2)
# s.dim()
# t.sleep(2)
# s.dim()
# t.sleep(2)
# s.dim()
# t.sleep(2)
# s.brighten()
# t.sleep(2)
# s.on()
