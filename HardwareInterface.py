class HardwareInterface:

    #sound effects should be a dictionary mapping ints to filepaths
    #of sound effects
    def __init__(self, sound_effects):
        self.sound_effects = sound_effects

    #sound will be an int referencing a preset list of effects
    def playSound(self, sound):
        print("Playing sound " + str(sound))

    #does text to speak on an inputted text
    def speak(self, text):
        print("Speaker says: " + text)

    #does the led controls
    def flash(self, color):
        pass