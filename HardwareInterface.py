
class HardwareInterface:

    #sound effects should be a dictionary mapping ints to filepaths
    #of sound effects
    def __init__(self, sound_effects):
        self.sound_effects = sound_effects

    #sound will be an int referencing a preset list of effects
    def playSound(self, sound):
        pass

    #does text to speak on an inputted text
    def speak(self, text):
        pass

    #does the led controls
    def flash(self, color):
        pass